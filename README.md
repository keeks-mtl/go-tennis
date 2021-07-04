# Go-Tennis

## Goal For This Project

Go-Tennis is a place that helps facilitate a love of tennis for those in the community. This lesson first space, 
creates an environment where people can become better tennis players and cater to their needs to do so. 
First and foremost it is about teaching proper skills in tennis through lesson for all skill levels through 
either a pay per lesson model or subscription based model. In order to become better tennis players it helps 
having access to tennis merchandise which the community can through the shop feature. Another important part 
of becoming a better tennis player is regular practice. Go-Tennis allows those registered to set up matches 
to make sure they get their practice in and their skills up to par. 

## Table of Contents


## UX

### User Stories
#### Viewing and Navigation
- As a user, I want to easily navigate the site in an intuitive way.
- As a user, To view list of products
- As a user, I want to quickly identify product categories. 
#### Registration and User Accounts
- As a user, I want a clear & easy way to register and join.
- As a user, I want to easily log in with my username and password.
- As a user, I want to see my profile and what I've bought or scheduled.
- As a user, I want to easily and quickly log out.
- As a user, I want to recover my password in case i forget it.
- As a user, I want to receive email confirmation after reqgistering.
- As a user, I want to have a personlised user profile.  
#### Sorting and Searching
- As a user, I want to sort the list of available products
- As a user, I want to sort a specific category of product
- As a user, I want to search for a procut by name.
#### Information
- As a user, I want to find out more about Go-Tennis on social media. 
- As a user, I want to find where the lessons are located.
- As a user, I want to be prepared for lessons with tennis equipment. 
- As a user, I want to be able to know about the coaches I might hire.
- As a user, I want to know what other people think of the coaches.
- As a user, I want to see what the lessons entail.
- As a user, I want to know what the pricing of the lessons are.
- As a user, I want to know what the lesson schedule looks like.
- As a user, I want to know about the users I might play. 
- As a user, I want to be able to stay informed of changes/opportunities. 
#### Purchasing and Checkout
- As a user, I want to easily select size and quantity of a product when purchasing it. 
- As a user, I want to be able to find what tennis equipment I am looking for easily. 
- As a user, I want to be able to see individual product details, price, and images.
- As a user, I want to be able to buy equipment easily and clearly. 
- As a user, I want to be able to book a lesson.
- As a user, I want to be able to schedule matches with other players.
- As a user, I want to view items in my bag to be purchased.
- As a user, I want to adjust the quantity of individual items in my bag.
- As a user, I want to feel my personal and payment information is safe and secure.
- As a user, I want to view order confirmation after checkout.
- As a user, I want to receive email confirmation after checking out. 

- As a user, I want to be able to cancel a class or match.
- As the site owner, I want users to be able to use my site easily.
- As the site owner, I want to be able to promote my shop. 
- As the site owner, I want to easily change products and subscription options easily.
- As the site owner, I want to easily add products and pricing options easily.
- As the site owner, I want to delete products and subscription options easily 
- As the site owner, I want to be able to see schedules and class sizes. 
- As the site owner, generate more business through webshop, subscription service, and single purchases/matches.


### Design Choices

- The site is based around tennis and the particular logo for the site. 
- The site itself needed to be easy to navigate, provide information users would find beneficial, and displays
    said information in a way that is visually appealing. 
- The overall design choice created a space that was malleable and gave space for an ecommerce functionality and community. 
- The colour choices were centered around the logo and matched through [color.adobe](https://color.adobe.com/create/color-wheel)
    to find all colours in the logo.  
- The palette worked well at feeling familiar with know tennis colours but also felt fun. 
- [Figma](https://www.figma.com) was used to create the wireframes and organise how the site flowed. 
- Figma also helped visualise how the different pages would look on different screen sizes. 
- Once the project was built following the planning stages, there were ways that the design changed while building the site.
    Because my background isn't in design, it is hard to come up with something that appeals visually from a blank slate.
    The design process was an evolving process that required tweeks and changes to improve Go-Tennis and create something
    that looked appeasing. 

### Fonts

- The goal was to have a crisp and modern feel with a bit of punch. 
- [Google Fonts](https://fonts.google.com/)

### Icons

- Go-Tennis takes advantage of iconography by utilizing icons from [Font Awesome](www.fontawesome.com).
- Many of the buttons use icons to give a clear visual cue to solidify what the buttons do. 
- The icons made the content more concise and didn't distract from the information.
- An important icon used, is the hamburger icon that will make navigation more simple on mobile devices.
- Social media icons are also used to give clear indication of how to follow Go-Tennis on social media.
- The logo and favicon was chosen for it's simple representation of tennis. 

### Colours

- The colour theme included six main colours that complimented one another.
- The colours were chosen because of their contrast and matched with the logo.
- Buttons were also color coded in a way that intrinsically implied what they accomplished. A red
    to cancel or delete and a green to add/go forward. 

### Wireframes

- The wireframes that were used to initially design each page are below:
    - link


## Features Implemented

### Navigation

- The navigation bar was created using Bootstrap to ensure that it was fully responsive.
- An example of a responsiveness change includes a hamburger menu when viewed on smaller viewports and the
    search icon and cart icon.
- The navigation bar shows Profile, Coaches, Lessons, Book, Matches, Shop and Logout when a user is logged in. 
- When a user who is not logged in visits the navigation bar shows: Coaches, Lessons, Book, Shop, Register, and Login. 

### Pagination

- The feature is used to make sure pages aren't filled with shop products and slowing down users' viewing. 
- The main shopping page displays 12 products and displays the products on serveral pages. 

### Home Page

- Firstly displays an hero image to evoke a feeling and get a sense of playing tennis. 
- Gives users a brief description of what Go-Tennis offers. 
- A call to action through a link to the shopping page to buy equipment. 
- Another call to action through the join newsletter button. 

### Register

- The registration page allows users to register to use all of Go-Tennis' features.
- The registration form requires all of the following information to create an account:
    - User's first name 
    - User's last name
    - User's email
    - User's username
    - User's password
- All the data is then stored in a "users" collection in the database.
- The passwords are hashed.
- Once the register form is completed and the data is stored the user is redirected to their
    profile page and a flash message appears letting the users know their registration is succesful. 

### Log In

- Returning users who have already registered can use the log in form to 
    access Go-Tennis and their account. 
- The form requires a username and password which is then checked against their
    credentials stored in the database.
- If username or password is incorrect the user is flashed a message letting them know 
    username and/or password is incorrect. 
- Succesfully filling the form takes the user to their profile page. 

### Profile Page

- The profile page allows users to see their order history, their already scheduled lessons,
    and any matches they have scheduled. 
- Each subsection of the profile page is ordered my date (either ascending or descending). 
- The Profile page shows the user's username and users also have the ability to change things 
    they have scheduled.  

### Coaches Page

- The coaches page has the coaches names and images of the coaches. 
- The coaches page shows visitors information on tennis coaches history.
- The coaches page also shows ratings for the coaches based on user's who have had lessons. 
- User's can access the page through the navigation bar and is available to all visitors.

### Lessons Page

- The lessons page shows users the different lesson options available to them.
- The lessons are divided into group lessons by skill level and solo private lessons. 
- The lessons page also includes pricing by either pay per class or a training program. 
- The lessons page training programs are linked to a payment page and the pay per class is linked to 
    the book page. 

### Book Page

- A user can only use the book page when they are logged in.
- The book page shows a calendar which has what classes are available and gives them the option to choose
    one and book a slot.
- If the user is on a training program they will be given the option to confirm the booking but not required
    payment. 
- If the user is following the pay per class option they will be redirected to the payment page where they 
    will have to confirm their information and follow through with payment. 

### Matches Page

- The matches page is only available to users who have logged in
- Users are given credits after each lesson they've had to be used to 'pay' for a match or they can 
    pay for the court through this page. 
- The matches page will have a table that shows the available courts and if any players have booked the court.
- It will include the date, time, what type of match (singles or doubles), and what players have commited to the 
    game and their skill levels as well as being able to link to their profile page.

### Shop Page

- The shop page is available to everyone. 
- The shop page opens with all products listed by rating.
- There will be 3 badges at the top with the 3 product lines available in the product shop.
- The users will have the ability to sort through the products by price, rating, and newest products. 
- The shop can be filtered by the 3 product lines, tennis balls, tennis rackets, and tennis racket bags.
    the last two of which can be sorted by sizes. 

### Rating Coaches Functionality

- A user has the ability to rate coaches if they've had lessons with said coach. 
- A user can only rate a coach once.  
- *maybe testimonials. 

### Search

- There will be the ability to search for a few keywords across the entire site.
- The search icon will be on the navigational bar on mobile devices for quick access. 

### Log out

- The log out functionaly is located on the navigational bar and allows users 
    the ability to log out when clicked.
- The user when logged out is redirected to the log in page with a flash message
    that informs them they have been logged out. 

### Features Left to Implement

- Comment section for registered users to discuss the plants and share tips.
- Private messaging abilities for members to message other members to share information
    privately.
- Abiltiy to undo a "like".
- Afiliate links to plant shops so users can buy plants they've seen.
- Share plant ability (share plant card through social media).
- To check in realtime on register form if the username already exists. 

## Database Design

During the development stage I worked with Django's default sqlite3 database.
- The collections are associated with one another through the following ways:
    - 

## Data Modelling

### Products App
#### Products
| Name | Key | Validation | Field Type |
--- | --- | --- | --- 
SKU | sku | max_length=254 | models.CharField 
Name | name | `maxlength="50"` | models.CharField
Description | description | `` | models.TextField
Price | price | max_digits=6, decimals_places=2 | models.DecimalField
Image_url | image_url | max_length=1024, null=True, blank=True | models.URLField
Image | image | upload_to='', null=True, blank=True, on_delete=models.SET_NULL | models.ForeignKey
Rating | rating | max_digits=6, decimals_places=2, null=True, blank=True | models.DecimalField
Has_sizes | has_sizes | default=False, null=True, blank=True | models.BooleanField

#### Category

| Name | Key | Validation | Field Type |
--- | --- | --- | --- 
Name | name | max_length=254 | models.CharField 
Friendly_name | friendly_name | `maxlength="254", null=True, blank=True` | models.CharField

### Profile App
#### User Profile

| Name | Key | Validation | Field Type |
--- | --- | --- | --- 
User | user | User, on_delete=models.CASCADE | models.OneToOneField 
Phone Number | default_phone_number | `maxlength="20", null=True, blank=True` | models.CharField
Street Address 1 | default_street_address1 | `maxlength="80", null=True, Blank=True` | models.CharField
Street Address 2 | default_street_address2 | `maxlength="80", null=True, Blank=True` | models.CharField
Town or City | default_town_or_city | `maxlength="40", null=True, Blank=True` | models.CharField
County, State or Locality | default_county | `maxlength="80", null=True, Blank=True` | models.CharField
Postcode | default_postcode | `maxlength="20", null=True, Blank=True` | models.CharField
Country | default_country | blank_label='Country', null=True, Blank=True` | CountryField
Rating | rating | max_digits=6, decimals_places=2, null=True, blank=True | models.DecimalField
Skill Level | skill_level | max_digits=6, decimals_places=2, null=True, blank=True | models.CharField
Role| role | maxlength="40", null=True, Blank=True | models.CharField

### Checkout App
#### Order

| Name | Key | Validation | Field Type |
--- | --- | --- | --- 
Order Number | order_number | maxlength="32", null=False, editable=False | models.CharField 
User Profile | user_profile | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders"` | models.ForeignKey
Full Name | full_name | `maxlength="50", null=True, blank=True` | models.CharField
Email | Email | `maxlength="254", null=True, blank=True` | models.CharField
Phone Number | phone_number | `maxlength="20", null=True, blank=True` | models.CharField
Street Address 1 | street_address1 | `maxlength="80", null=True, Blank=True` | models.CharField
Street Address 2 | street_address2 | `maxlength="80", null=True, Blank=True` | models.CharField
Town or City | town_or_city | `maxlength="40", null=True, Blank=True` | models.CharField
County, State or Locality | county | `maxlength="80", null=True, Blank=True` | models.CharField
Postcode | postcode | `maxlength="20", null=True, Blank=True` | models.CharField
Country | country | blank_label='Country', null=True, Blank=True` | CountryField
Date | date | auto_now_add=True | models.DateTimeField
Delivery Cost | delivery_cost | max_digits=6 , decimal_places=2, null=False, default=0 | models.DecimalField
Order Total | order_total | max_digits=10 , decimal_places=2, null=False, default=0 | models.DecimalField
Grand Total | grand_total | max_digits=10 , decimal_places=2, null=False, default=0 | models.DecimalField
Original bag | original_bag | null=False, Blank=False | models.TextField
Stripe Pid | stripe_pid | `maxlength="254", null=False, Blank=False | models.CharField

#### Order Line Item

| Name | Key | Validation | Field Type |
--- | --- | --- | --- 
Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | models.ForeignKey 
Product | product | Product, on_delete=models.CASCADE, null=False, blank=False | models.ForeignKey
Quantity | quantity | null=False, blank=False, default=0 | models.IntegerField
Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | models.DecimalField

### Lessons App
#### Lessons

| Name | Key | Validation | Field Type |
--- | --- | --- | --- 
Lesson id | lesson_id | max_length=32, null=False, blank=False, on_delete=models.CASCADE | models.CharField 
Type | type | max_length=32, null=False, blank=False | models.CharField
Coach | coach | Profile, maxlength="40", null=True, blank=True | models.ForeignKey
Date | date |  | models.DateTimeField 
Time | time | max_length=32, null=False, blank=False | models.DateTimeField 
Spots | spots | null=False, blank=False, default=0 | models.IntegerField
Skill Level | skill_level | max_length=32, null=False, blank=False | models.CharField 
Students | students | Profile, max_length=32, null=True, blank=True | models.ForeignKey  

## Technologies Used

### Languages, Libraries and Frameworks

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - The base of the code for the overall structure of the site.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used for the styling of the site.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [JQuery](https://jquery.com/)
    -  
- [Python](https://www.python.org/)
    - used to write the logic that operates the site.
- [Font Awesome](https://fontawesome.com/)
  - For the icons used throughout the site.
- [Bootstrap](https://getbootstrap.com/)
  - Was used for added styling and responsiveness of the project.
- [Django](https://www.djangoproject.com/)
    - To construct and render pages.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    -  Simplify how data is displayed from the backend of this project in html.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - A collection of libraries used to create a WSGI compatible web application in Python.
- [Google Fonts](https://fonts.google.com/)
  - Used to import the main fonts for the styling of the project.
- [PyMongo](https://pypi.org/project/pymongo/)
    - To help MongoDB and Python communicate. 

### Tools

- [Github](https://github.com/)
  - Version control and recording of all changes to site during development process.
- [Gitpod](https://gitpod.io/)
  - The IDE used for developing this project.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
  - Used to debug code and show styling changes before changing the actual code.
- [Balsamiq](https://balsamiq.com/)
  - Used for creating the wireframes in the planning stage.
- [W3C HTML Validator](https://validator.w3.org/)
  - Used as a HTML validator.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - Used as a CSS validator.
- [JSHint](https://jshint.com/)
    - Used to test JS to ensure there were no errors.
- [PEP8 Online](http://pep8online.com/)
    - Used to check Python was PEP8 compliant.
- [WAVE](https://wave.webaim.org/)
    - Used to test accesibility of site.
- [SQlite3](https://www.sqlite.org/index.html)
    - Used for database functionality in development.
SQlite3 - development database.
- [Heroku](https://www.heroku.com/home)
    - Used to host the site
- [Stripe](https://stripe.com/gb)
    - To facilitate card payments
- [AWS S3](https://aws.amazon.com/)
    - To store static and media files in production



- [Favicon](https://favicon.io/)
    - Used to generate the Favicon on the webpage tab.
- [AmIResponsive](http://ami.responsivedesign.is/#)
    - Used to create responsive images.

## Testing

Testing information can be found in this file : [testing.md](testing.md)

## Deployment

### Local Deployment
#### Requirements

- An IDE (such as Gitpod or Visual Studio Code)
- Python3
- PIP3
- MongoDB 

#### Instructions

- Open your IDE and in your terminal and clone the git repository with the following command.
    - git clone https://github.com/keeks-mtl/petiole
- Create environment file called "env.py" and add :
    - MONGO_URI= mongodb+srv:// (and link to your database)
    - SECRET_KEY= <your secret key>
- Add your env.py to your .gitignore. so it's not uploaded to github at any point.
- Upgrade pip locally with the command:
    - "pip install -U pip"
- Install the modules used to run the application using in your terminal:
    - "pip freeze > requirements.txt"
- In app.py, switch debug=False to debug=True
- Create a MongoDB account and create a database called "petiole"
- Create the following collections:

users
```
fill out later
```

plants
```
fill out later
```
- you can now run the application with the command
```
python3 app.py
```
- you can visit the website now at 
```
http://127.0.0.1:5000
```

### Heroku Deployment

- Open your IDE and in your terminal and clone the git repository with the following command.
```
git clone https://github.com/keeks-mtl/go-tennis
```
- create a requirements.txt file using the terminal command
```
pip freeze > requirements.txt
```
- Create a Procfile with the terminal command 
```
echo web: python app.py > Procfile
```
- 'git add' and 'git commit' the new requirements and Procfile and then 'git push'
    to GitHub
- Create an account on [Heroku](https://www.heroku.com/home)
- Create a new app on Heroku by clicking the "New" button in your dashboard and then 'Create New App'.
- Give the app an unique name and set the region.
- In the dashboard for your new app, click on "Deploy" > "Deployment method" and select GitHub
- Confirm the linking of the Heroku app to the correct GitHub repository.
- In the heroku dashboard for the app, click on 'Settings' > 'Reveal Config Vars'
- Set the following config vars:
```
IP = 0.0.0.0
PORT = 5000 
SECRET_KEY = `<your_secret_key>`
```
- in the Heroku dashboard, click "Deploy"
- Make sure master branch is selected and then click "Deploy Branch"

## Credits

### Content - Media -Inspiration

I have used the following websites to get info & images for my website.

#### Images
- [Pixabay](https://pixabay.com/)
- [Unsplash](https://unsplash.com/)
- [Pexels](https://www.pexels.com/)

#### Information
- 

#### Code
- [PrettyPrinted Youtube Channel](https://www.youtube.com/watch?v=I2-JYxnSiB0&ab_channel=PrettyPrinted)
    - django forms date picker

### Acknowledgements

- A special thank you to my mentor Antonija Simic for her help in going through my project thoroughly and guiding me through what 
    is expected of my website and how to clean up my code.
- The Code Institute Slack community for their technical support.

## Disclaimer
This website is for educational purposes only. 