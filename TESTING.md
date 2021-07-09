# Petiole - Testing

[Main README.md file](README.md)

[View website on Heroku](go-tennis.herokuapp.com/)

## Table of Contents

## User Stories Testing

### Viewing and Navigation
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| As a user, I want to easily navigate the site in an intuitive way| Navigation is obvious and clear with links recognisable to users  | checked |
| As a user, I want to view list of products | All products appear so user can see them  | checked |
| As a user, I want to quickly identify product categories | Product categories are front and center so users and see them clearly  | checked |

### Registration and User Accounts
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| As a user, I want a clear & easy way to register and join | Register form is easy to find and linked to when things require an account & form is easy and quick to fill  | checked |
| As a user, I want to easily log in with my username and password | Log in form is clear and easy to fill out with validations | checked |
| As a user, I want to see my profile and what I've bought or scheduled | There's a profile page that shows products and lessons bought  | checked |
| As a user, I want to easily and quickly log out | Log out is easy and quick  | checked |
| As a user, I want to recover my password in case i forget it | A link on login in page to reset password and a form that easy to fill out | checked |
| As a user, I want to receive email confirmation after registering | Email confirmation is sent after registering | checked |
| As a user, I want to have a personlised user profile | Profile page is personalised to each user showing their username and information | checked |

### Sorting and Searching
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| As a user, I want to sort the list of available products | A sort bar is easily found and has sorting options that work | checked |
| As a user, I want to sort a specific category of product | Ability to just view a particular product category line | checked |
| As a user, I want to search for a product by name | A search bar that works and finds specific products | checked |

### Information
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| As a user, I want to find out more about Go-Tennis on social media | Social media icons are easily found and links to them open in a new tab | checked |
| As a user, I want to find where the lessons are located | There is a map and address of Go-Tennis | checked |
| As a user, I want to be prepared for lessons with tennis equipment | It is easy to shop and there are links to the shop around Go-Tennis | checked |
| As a user, I want to be able to know about the coaches I might hire | There is a page with information on the coaches | checked |
| As a user, I want to know what other people think of the coaches | There are comments and ratings of coaches | checked |
| As a user, I want to see what the lessons entail | There is a page with descriptions of the lessons | checked |
| As a user, I want to know what the pricing of the lessons are | There is pricing of the lessons before booking the lesson | checked |
| As a user, I want to know what the lesson schedule looks like | It is easy to see the date & time of the lessons | checked |

### Purchasing and Checkout
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| As a user, I want to easily select size and quantity of a product when purchasing it | There is a button/option to select size & quantity | checked |
| As a user, I want to be able to find what tennis equipment I am looking for easily | There are options to filter and sort products in the shop | checked |
| As a user, I want to be able to see individual product details, price, and images | There is a product details page that shows information on a particular product | checked |
| As a user, I want to be able to buy equipment easily and clearly | It is easy to add products to the bag and checkout | checked |
| As a user, I want to be able to book a lesson | It is possible to add a lesson to the bag and checkout | checked |
| As a user, I want to view items in my bag to be purchased | There is a bag page where everything in the bag is clearly shown | checked |
| As a user, I want to adjust the quantity of individual items in my bag | On the bag page there is an option to change quantities of an item or remove it | checked |
| As a user, I want to feel my personal and payment information is safe and secure | There is a secure checkout page | checked |
| As a user, I want to view order confirmation after checkout | There is a page that lets the user know they've successfully finished payment of their order | checked |
| As a user, I want to receive email confirmation after checking out | An email is sent to the user once they've finished payment | checked |

### Site Owner
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| As the site owner, I want users to be able to use my site easily | Everything is clear and navigatable | Checked |
| As the site owner, I want to be able to promote my shop | There are links to the shop around Go-Tenis and links to social media for presence | Checked |
| As the site owner, I want to easily add products, lessons, and coaches easily | There are pages to add products, lessons, and coaches | Checked |
| As the site owner, I want to easily change products, lessons, and coaches easily | There are pages to update products, lessons, and coaches which automatically update the info accross the site | Checked |
| As the site owner, I want to delete products, lessons, and coaches easily | There is the option to delete products, lessons, and coaches with confirmation to ensure it isn't done by accident | Checked |
| As the site owner, generate more business through webshop and single purchases | There is a shop that is easy to navigate and buy from | Checked |

## Code Validators
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - No errors, the results are below:
  <img src="./static/images/readme/cssvalidator.png"/>

- [W3C HTML Validator](https://validator.w3.org/)
- [Pep8Online](http://pep8online.com/)
    - No errors, the results are below:
    <img src="./static/images/readme/pep8.png"/>
- [JSHint](https://jshint.com/)
    - No issues reported on script.js, results are below:
    ```
    Metrics
    There are 3 functions in this file.
    Function with the largest signature take 1 arguments, while the median is 1.
    Largest function has 3 statements in it, while the median is 3.
    The most complex function has a cyclomatic complexity value of 2 while the median is 1.
    ```
## Manual Testing

### Elements on Every page

1. Navbar
- Check navbar when not logged in and make sure all proper links are showing.
  - Click on all the links and make sure they redirect to the proper pages.
- Check navbar when logged in and make sure all the proper links are showing.
  - Click on all the links and make sure they redirect to the proper pages
- Check the navbar on all screen sizes and make sure it is responsive and the navbar changes on the different screen sizes. 
- Make sure footer is at the bottom of the page on all pages (make sure to check pages with less content like login page)

2. Footer
- Click on all social media links and make sure they open in a new tab.
- Click on the email address and make sure it is a link to email that email address.
- Click on the phone number and make sure the phone dialer opens up with that number.
- Check the spacing and links in all device sizes for responsiveness.
- Make sure footer is at the bottom of the page on all pages on all device sizes (especially pages with less content like log in page)

### Home Page
#### General Testing
- Click on all the links and make sure they take you to where they are supposed to.
  - Lessons page
  - Coaches page
  - Shop page
  - Book lesson page
  - Google maps for Clissold Park
  
#### Responsiveness Testing
- Check the home page on all device sizes and make sure everything is well spaced on all size screens

### Search Bar
#### General Testing
- Do a search for words in the description of a product and make sure it appears.
- Do a search for a word that does not appear in any product name or description and make sure nothing shows on the shop page. 
- Do a search for a name of a product and make sure it appears.

#### Responsiveness Testing
- Make sure search bar is visible on all screen sizes. 
- On smaller screens make sure the drop down appears to enter the search. 

### Register
#### General Testing
- Make sure both log in links goes to log in page
- Make sure email validation works
- Make sure username validation works
- Make sure validation works to ensure both passwords are the same. 
- Check that once the form is properly filled out the log in button takes the user to the email verification page.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Login
#### General Testing
- Check the sign up link works.
- Check the home button works.
- Check that the forgot password link takes the user to the password reset page.
- Make sure the form validations work
- Make sure when the log in information is incorrect that the form tells the user that the password OR username is correct. 
- Check that when a user logs in with the proper information that the page is redirected to the home page. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Logout
#### General Testing
- Check that if the cancel button is pressed that the user is redirected to the home page and they are still logged in. 
- If The user presses the log out button make sure they are redirected to the home page and they are informed that they have been logged out. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Coaches Page
#### General Testing
- Click on the book lesson with "" button and make sure it redirects to the book lesson page with only that coach's lessons.
- Check that the edit and delete links only are shown to the superuser.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Coach Page
#### General Testing
- Check that the book lesson with "" button is linked to the book lesson page but only shows lessons with that coach. 
- Make sure that the edit and delete links are only visible to the superuser. 
- Make sure that the comments feature is visible. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Comment Feature
#### General Testing
- Make sure comments are shown first and that the comment form is after.
- Check that the comments form is properly validated.
  - Must have comment 
  - Stars can only be in the range of 1-5
- Make sure once a comment is submitted the user is redirected to the coach page with a toast informing them that the comment was successful.
- Check that all rating options show correct amount of stars.
- Make sure comment automatically has the date and user who submitted the comment. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Coach Management Page
#### General Testing
- Check the add coach form validation works on all the required fields
- Make sure the cancel button redirects to coaches page. 
- Once the form is properly filled and sent, make sure the user is redirected to the new coach's page and the a toast lets the user know they succesfully added a coach.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Edit Coach Page
#### General Testing
- Check that a toast let's the user know they are currently editing a user. 
- Check that the edit coach form is prepopulated with the information on the coach. 
- Make sure the form validations still work. 
- Once the form is submitted make sure the user is redirected to the coach's page.
- Make sure only the superuser can access the page. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Delete Coach Feature
#### General Testing
- Make sure the delete coach link on the coaches page and coach page both make the delete confirmation modal appear. 
- Make sure the delete modal's information is correct. 
- Once the delete button on the delete modal is pressed, make sure the correct coach is deleted and that a toast shows the user that they have succesfully deleted the coach. 
- Make sure only the superuser can access the route.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Lessons Page
#### General Testing
- Make sure all the links on the page take the user to the specific page.
  - Coaches but to coaches page
  - Book a Lesson button to the book page
  - Book now button the the respective book page with only that class type shown.
  - Shop now button to the shop page. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Book Lesson Page
#### General Testing
- Check that the class type badges show only the respective lessons of that class type.
- Check that the Coach names badges show only the respective lessons by that coach.
- Make sure the all lessons button resets the page to show all the lessons.
- Check that the sort dropdown correctly sorts the lessons by each sort option
- Make sure the display that states how many lessons are being shown is correct.
- Check that the book lesson button is putting the correct lesson in the user's bag.
- Make sure the toast is stating the correct lesson is in the shopping bag. 
- Make sure the shop now button redirects the user to the shop page. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Lesson Management Page
#### General Testing
- Check that date picker and time picker work
- Make sure form validations on add lesson form work
- Check that the cancel button takes the user back to the lessons page
- Once the form is properly filled and submitted make sure the user is redirected to the lesson management page and a toast lets the user know they have successfully added the lesson. 
- Make sure the lesson management page can only be accessed by an administrator. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Edit Lessson Page
#### General Testing
- Check that the form validations work.
- Check that cancel button takes the user back to the book lesson page.
- Make sure the form can only be accessed by an administrator. 
- Once the form is properly filled out and submitted, the user should be redirected to the book lesson page and a toast should tell the user they have successfully edited a lesson. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Delete Lesson Feature
#### General Testing
- Make sure the delete button on the book lesson page activates a delete modal to confirm deletion. 
- Check that the information displayed in the delete modal is correct.
- Once an administrator has clicked the delete button on the delete modal, make sure the right lesson is deleted and a toast lets the user know they deleted a lesson. 
- Check that the delete lesson route is protected.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Shop Page
#### General Testing
- Check that pressing on the product category badge shows only those products in that category to the user.
- Make sure the products home button resets the products to show all the products in their default sorting option
- Check each individual sorting option sorts the products in the correct order. 
- Check that the edit and delete links are only shown to the superuser.
- Make sure the up arrow in the bottom right corner of the screen takes the user back up to the top of the page. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.
- That the products are in columns of 4, 3, 2, and 1 depending on the screen size.

### Product Detail Page
#### General Testing
- Check that the information is all correctly displayed.
- Make sure the product category badge redirects the user to the shop page with that product category displayed.
- Make sure that the edit and delete links are only displayed to the superuser. 
- Check that the size dropdown allows users to choose a size of only the products that has sizes.
- Make sure the quantity box has validattions. 
- Check that the keep shopping button redirects the user to the shop page. 
- Make sure the add to bag button adds the product to the user's bag and that the user sees a toast that lets the user know they successfully added that product to their bag. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Product Management Page
#### General Testing
- Make sure form validations on add product form work
- Check that the cancel button takes the user back to the products page
- Once the form is properly filled and submitted make sure the user is redirected to the product detail page of that product and a toast lets the user know they have successfully added a product. 
- Make sure the product management page can only be accessed by an administrator. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Edit Product Page
#### General Testing
- Make sure there is a toast that informs the user they are editing the product
- Check that the form is prepopulated with the information on the product
- Check that the form validations work.
- Check that cancel button takes the user back to the products page.
- Make sure the form can only be accessed by an administrator. 
- Once the form is properly filled out and submitted, the user should be redirected to the product detail page and a toast should tell the user they have successfully edited the product. 
 
#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Delete Product Feature
#### General Testing
- Make sure the delete button on the product detail page & products page activates a delete modal to confirm deletion. 
- Check that the information displayed in the delete modal is correct.
- Once an administrator has clicked the delete button on the delete modal, make sure the right product is deleted and a toast lets the user know they deleted a lesson. 
- Check that the delete lesson route is protected.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Bag Page
#### General Testing
- Add one lesson to shopping bag and then go to bag page.
  - Make sure the correct information is displayed in the toast.
  - Check that the correct information is displayed on lesson info table.
  - Make sure shop total isn't displayed
  - Make sure there is no delivery cost.
  - Check that the grand total is correct.
  - Make sure the remove link removes the lesson from the bag and a toast appears to tell the user that the lesson has been removed from the bag.
  - Click the secure checkout button and make sure you are redirected to checkout page
  - Make sure when the bag is empty the page lets the user know the bag is empty. 
- Add a single quantity of one into the shopping bag, 2 of another product, 1 product a product with a size and 2x of another product with a size and then go to the bag page.
  - Make sure the correct information is displayed in the toast.
  - Make sure all the products have the correct information displayed about the product info. 
  - Make sure all the subtotals are correct.
  - Make sure the remove link removes the product from the bag and a toast informs the user that the product has been removed. 
  - Make sure the validations for the quantity increment/decrement button validations work.
  - Make sure the update button updates the quantity of the product in the bag and a toasts informs the user that the quantity has been updated.
  - Make sure shop total, delivery, and Grand Total are correct. 
  - Click the secure checkout button and make sure you are redirected to checkout page
- Make sure the keep shopping button redirects the user to the shop page.
- Add a lesson and a product to a user's shopping bag and navigate to the bag page. 
  - Make sure both lesson and product are in the shopping bag.
  - Make sure all the information is correct. 
  - Make sure Lesson total, Shop Total, Delivery, and Grand Total are correct.
  - Click secure checkout and make sure the user is redirected to the checkout page.

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Checkout Page
#### General Testing
- Make sure order summary has the correct information. 
- Make sure Shop total & delivery only show if there is a product (and delivery is below the threshold)
- Make sure lesson total only shows if there is a lesson.
- Check that the checkout form is visible and prepopulated with any information that is in the database already about the user. 
- Make sure the form validations work
- Check that the adjust bag button takes the user back to the bag page. 
- Once the form is properly filled out make sure the loading overlay appears and the user sees a toast that the purchase was successful. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Checkout Success Page
#### General Testing
- Click on the "take a look at our products" button and see if the user is redirected to the products page. 
- Make sure sure the heading says 'thank you, ?' where the ? is the user's full name. 
- Check the chart and make sure all the information form the purchase is correct. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Profile Page
#### General Testing
- Make sure the validations on the default delivery information work
- Make sure the information is updated when the update information button is pressed. 
- Check that the order history table is correct. 
- Click on an order number and make sure the user is redirected to an order summary page. 

#### Responsiveness Testing
- Make sure page is responsive and works on all device sizes.

### Pagination Feature
#### General Testing


## Bugs

### Checkout order total not correct Bug
#### Bug
- The grand total on the checkout success page and the order admin wasn't correct
#### Fix
- add lesson_lineitem_total to the checkout model order

### lesson cost Bug
#### Bug
- the lesson cost doesn't show on the checkout_success.html when only a lesson is bought but shows when a lesson & product is bought. 
#### Fix
- fix description

### Bugname Bug
#### Bug
- bug description
#### Fix
- fix description

### Bugname Bug
#### Bug
- bug description
#### Fix
- fix description
