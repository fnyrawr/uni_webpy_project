from fpdf import FPDF
import random
from datetime import date
import datetime
from collections import Counter
from django.conf import settings

class PDF(FPDF):
    def __init__(self, *args, data=[], user="", email="", payment=""):
        super().__init__(*args)
        self.set_auto_page_break(auto=True, margin=15)
        self.alias_nb_pages()
        self.set_font('helvetica', 'BIU', 16)
        self.set_font('Arial', '', 12)
        self.order_number = "{}-{}-{}".format(random.randint(100, 999),
                                              random.randint(4000000, 9999999),
                                               random.randint(8000000, 9999999))
        self.order_date = date.today()
        self.order_date_str = date.today().strftime("%B %d, %Y")
        self.data = data
        self.order_price = 42
        self.user = user
        self.email = email
        self.payment = payment
        self.set_price()
        self.passing_data()
        self.fill_page()
         # self.output('Invoice.pdf')

    def header(self):
        print(".." + settings.STATIC_URL + "images/amyzonelogo.png")
        #self.image("amyzonelogo.png", 10, 20, 52, 12)
        self.set_font('helvetica', 'B', 20)
        self.cell(80)
        self.set_font('Arial', '', 10)
        self.cell(30, 10, "Amyzone.com - Order {}".format(self.order_number), ln=1, align='C')
        self.ln(20)
        self.cell(80)
        self.set_font('Arial', '', 15)
        self.set_text_color(134, 193, 0)
        self.cell(30, 10, "Final Details for Order #{}".format(self.order_number), ln=1, align='C')
        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 5, "Order Place: {}".format(self.order_date_str), ln=1, align='L')
        self.cell(0, 5, "Amyzone.com - order number: {}".format(self.order_number), ln=1, align='L')
        self.cell(0, 5, "Name: {}".format(self.user), ln=1, align='L')
        self.cell(0, 5, "Email: {}".format(self.email), ln=1, align='L')
        self.cell(0, 5, "Order Total: ${}".format(self.order_price), ln=1, align='L')
        self.ln(5)
        self.cell(0, 5, "Shipping Address:", ln=1, align='L')
        self.cell(0, 5, "Luxemburger Str. 10", ln=1, align='L')
        self.cell(0, 5, "13353 Berlin", ln=1, align='L')
        self.cell(0, 5, "Germany", ln=1, align='L')
        self.set_font('Arial', '', 15)
        self.ln(5)
        self.cell(80)
        self.cell(30, 10, "Shipped on {}".format(self.order_date + datetime.timedelta(days=1)), ln=1, align='C')

    def footer(self):
        self.set_y(-85)
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, "Payment information", ln=1, align='C')

        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, "Payment Method:", ln=1, align='L')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, self.payment, ln=1, align='L')
        self.cell(0, 5, '', ln=1, align='C')
        self.set_font('Arial', 'B', 10)

        self.cell(0, 5, "Billing address:", ln=1, align='L')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, "Shipping Address:", ln=1, align='L')
        self.cell(0, 5, "Luxemburger Str. 10", ln=1, align='L')
        self.cell(0, 5, "13353 Berlin", ln=1, align='L')
        self.cell(0, 5, "Germany", ln=1, align='L')

        self.cell(0, 5, 'To view the status of your order, visit the following page:', ln=1, align='C')
        self.cell(0, 5, 'https://www.dhl.de/de/privatkunden/dhl-sendungsverfolgung.html', ln=1, align='C')
        self.cell(0, 10, '', ln=1, align='C')
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', ln=1, align='C')

    def fill_page(self):
        self.add_page()

        line_height = self.font_size * 2.5
        col_width = self.epw / 4  # distribute content evenly
        for count, row in enumerate(self.data):
            for datum in row:
                if count == 0 or count == len(self.data) - 1:
                    self.set_font('Arial', 'B', 12)
                else:
                    self.set_font("Arial", size=12)
                self.multi_cell(col_width, line_height, datum,
                               new_x="RIGHT", new_y="TOP", max_line_height=self.font_size)
            self.ln(line_height)

    def passing_data(self):
        self.data = list(self.data)
        z = Counter(self.data)
        self.data = [("{}x{}".format(z[d], d[0]), float(d[1]) * z[d]) for d in self.data]
        self.data = list(set([(row[0], "", "", "${}".format(row[1])) for row in self.data]))
        self.data.insert(0, ("Product name", "", "", "Price"))
        self.data.insert(len(self.data), ("Total price", "", "", "${}".format(self.order_price)))

    def set_price(self):
        temp = 0
        for p in self.data:
            temp += float(p[-1])
        self.order_price = temp
        self.order_price = "{:.2f}".format(self.order_price)


if __name__ == "__main__":
    data = (
        ("Bla", "99.99"),
        ("Bla", "99.99"),
        ("Blubb", "99.99"),
        ("Fooo", "99.99"),
        ("Luuuu", "99.99"),
        ("Luku", "99.99"),
    )

    pdf = PDF('P', 'mm', 'Letter', data=data, user="Prof. Amy Siu", email="amy.siu@bht-berlin.de",
              payment="Girocard | DE02120300000000202051")
