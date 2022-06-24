# WebPy Project

Git Repo for our WebPy Semmesterproject

[[_TOC_]]

## Members

| Name | Student ID |
| ---------- | ---------- | 
| **Florian** | s51541 |
| **Erdenay** | s50312 |
| **Michael** | s89671 |
| **Eric** | s51052 |

### Status updates
To organize our work better we should try to claim tasks and write status updates:
- When implementing features please add the following to the line: `ToDo` `Name` `LastChange`
    - If a view is done mark with [x] so we don't do the same work twice ;)
- I would recommend using the following keywords as status:
    - `ToDo` not yet claimed / not yet started
    - `WIP` currently work in progress
    - `OnHold` work in progress but currently no active development
    - `Testing` work is basically done, currently testing the features before migrating
    - `Done` done and pushed to repository

Since not every code change will be pushed immideately this would make it easier for us to keep track of tasks. Discord is a good tool for communication but the chat can end up quite chaotic quickly as we know lol. Oh, and feel free to edit this readme.

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
- Price
- PDF file

Product PDF and ean should be auto generated

> `Finished` `Eric` `23.06.2022`

### Product Picture
- Product
- Picture

### CustomUsers
- Abstract User Attributes
- Role
- Picture

> `Finished` `Eric` `22.06.2022`

### Product Reviews
- User
- Product
- Rating (1 to 5 stars)
- ReviewTitle
- ReviewText

> `Finished` `Eric` `23.06.2022`

### ReviewRating
- User
- Review
- Rating (useful, useless)

> `Finished` `Eric` `23.06.2022`

### Complaints
- type
- User
- Review
- Text (why review is inappropriate)

> `Finished` `Eric` `23.06.2022`

### ShoppingCart
- ProcessID (internal counter)
- UserID
- STATUS:
    - new
    - ordered
    - delivered

> `ToDo` `Name` `03.06.2022`

### ItemsInCart
- ProcessID
- ProductID
- OrderCount

> `ToDo` `Name` `03.06.2022`

### Anmerkung
    Sicher, dass wir wirklich Eans drin haben wollen, ist einfach nur unnötiger Zusatz, der keinen wirklichen Mehrwert hat und es ergibt auch keinen Sinn eine Ean autmatisch zu generieren, weil das sonst den Sinn einer Ean (eindeutige Identifizierung in der EU) zerstört
## Functions
- [ ] Registration
    - [ ] (send mail for Verification)
    - [x] password (twice for confirmation)
    - [x] customer profile picture
- [ ] Product
    - [ ] Product View
        - [ ] edit product infos
        - [x] Product Information as PDF
        - [ ] (auto generate product information as pdf if no pdf is available)
        - [x] multiple pictures for product
    - [ ] Review
        - [ ] edit review
        - [x] give stars for product and write text
        - [x] delete own review
        - [x] others can mark review as useful or not 
        - [x] others can report review
    - [ ] Product Search by filters
        - [ ] filter by productName
        - [ ] filter by productDescription
        - [ ] filter by reviewRatings
- [ ] CustomerService-Portal
    - [ ] Restrict access by role check
    - [ ] Add new Products and PDFs
    - [ ] Change Products
    - [ ] Delete Products
    - [ ] Review Complaints
    - [ ] Edit Reviews for product
    - [ ] Delete Reviews for product
- [ ] ShoppingCart
    - [ ] Orders (past orders for user)
    - [ ] (fake Checkout)

## Process descriptions
### Verification process
Link in the registered e-mail directs back to a verification route. Here the user has to login for the first time with the registered credentials (username and password). After that the user is verified by e-mail and is allowed to use the website as a customer.

## ToDo:
- [ ] implementing database
    - [ ] migrating database
- [ ] implement views (see above)
    - [ ] implement file uploads
    - [ ] implement file downloads
- [ ] styling
- [ ] hosting
    - [ ] creating userdata
    - [ ] testing functionalities
