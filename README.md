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
- Pictures (using fileuploads)
- Price
- PDF files

Product information should be dynamically generated from the given data

> `ToDo` `Name` `03.06.2022`

### Users
- UserID
- Name, given name
- E-Mail
- Username
- Password
- Role
- Picture

> `ToDo` `Name` `03.06.2022`

### Roles
- RoleID
- RoleName
- Description

> `ToDo` `Name` `03.06.2022`

### Product Reviews
- ReviewID
- UserID
- ProductID
- Rating (1 to 5 stars)
- ReviewText

> `ToDo` `Name` `03.06.2022`

### ReviewRating
- UserID
- ReviewID
- Rating (true = useful, false = not useful)

> `ToDo` `Name` `03.06.2022`

### Complaints
- UserID
- ReviewID
- Text (why review is inappropriate)

> `ToDo` `Name` `03.06.2022`

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

## Process descriptions
### Registration process
Needed information:
- username (has to be unique in db)
- e-mail (twice for confirmation, has to be unique in db)
- password (twice for confirmation)

Mail is sent with a confirmation token to the given e-mail address.

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
