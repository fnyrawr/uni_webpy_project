# WebPy Project

Git Repo for our WebPy Semmesterproject

[[_TOC_]]

## Members

| Name | Student ID |
| ---------- | ---------- | 
| **Florian** | s51541 |
| **Erdenay** | s50312 |
| **Michael** | s????? |
| **Eric** | s????? |

## General overview

- Django Webpage for an Online Shop
> Presentation date: 29.07.2022

[Link to requirements](https://lms.bht-berlin.de/pluginfile.php/1760338/mod_resource/content/1/group_project_requirements.pdf)

## Database
### Products
- ProductID
- ProductName
- Description as text
- EAN (article number on barcode)
- Pictures (using fileuploads)
- Price
- PDF files

Product information should be dynamically generated from the given data

### Users
- UserID
- Name, given name
- E-Mail
- Username
- Password
- Role
- Picture

### Roles
- RoleID
- RoleName
- Description

### Product Reviews
- ReviewID
- UserID
- ProductID
- Rating (1 to 5 stars)
- ReviewText

### ReviewRating
- UserID
- ReviewID
- Rating (true = useful, false = not useful)

### Complaints
- UserID
- ReviewID
- Text (why review is inappropriate)

### ShoppingCart
- ProcessID (internal counter)
- UserID
- STATUS:
    - new
    - ordered
    - delivered

### ItemsInCart
- ProcessID
- ProductID
- OrderCount

## Views
### For Customers
- [ ] Registration
    - [ ] Verification
- [ ] Customer Portal
    - [ ] Changing basic data / password
    - [ ] Upload of profile picture
- [ ] Customer Profile
- [ ] Product List
    - [ ] Product Search by filters
        - [ ] filter by productName
        - [ ] filter by productDescription
        - [ ] filter by reviewRatings
    - [ ] Product Search by text
    - [ ] Product View
        - [ ] Product Information as PDF
- [ ] ShoppingCart
    - [ ] (fake) Checkout
- [ ] Orders (past orders for user)

### For CustomerService
- [ ] CustomerService-Portal
    - [ ] Restrict access by role check
    - [ ] Add new Products and PDFs
    - [ ] Change Products
    - [ ] Delete Products
    - [ ] Review Complaints
    - [ ] Edit Reviews for product
    - [ ] Delete Reviews for product

## ToDo:
- [ ] implementing database
- [ ] implement views (see above)
- [ ] implement file uploads
- [ ] implement file downloads
- [ ] styling
- [ ] hosting
- [ ] creating userdata
