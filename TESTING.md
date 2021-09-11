## **Testing**
___
___
### Table of Contents

  * [Code Validity](#code-validity)
  * [Testing User Stories](#testing-user-stories)
  * [Functionality Testing](#functionality-testing)
  * [Defensive Design Testing](#defensive-design-testing)
  * [Responsiveness](#responsiveness)
  * [Usability Testing](#usability-testing)
  * [Performance Testing](#performance-testing)
  * [Browser Compatibility Testing](#browser-compatibility-testing)


### Code Validity
___

- HTML Markup Validation - [pass](https://validator.w3.org/nu/)
  * All pages passed the validator except for errors and warnings due HTML validator not being able to recognize Jinja.
    Validation is done trhough URL a well and resulted in no errors.
- CSS Validation - [pass](https://jigsaw.w3.org/css-validator/)
- JavaScript Code Quality Tool JSHint - [pass](https://jshint.com/)
- PEP8 - [pass](http://pep8online.com/)


### Testing User Stories
___

  **Guest user**

* As a guest user of Air Bubble, who is visiting the site for the first time, I want to understand easily what the site is all about
  * The Home page features a 'Welcome' section to offer new visitors more information on what this site is about. It directly enables the user
    to search for the travel stories with keywords. It also lets user see all the added stories and a call for signup to register to the site.
* As a guest user of Air Bubble, I want to search for information related to the recent travels happened to the destination I want to travel.
  - The search box is clearly labelled and easily accessible from the Home Page.
* As a guest user of Air Bubble, I want to be able to ask more questions related to a particular user travel story without signing up.
  - Clicking on Read More on any travel story lets the user read all info and let user comment on the story , there by letting 
    interact with the other users and the original author of the story.
* As a guest user of Air Bubble, I want to be able to easily access all available website features from different screen size devices.
  - The website is fully responsive and designed to provide an optimal user experience, no matter what device users are accessing it from.
* As a guest user of Air Bubble, I want to be able to sign up easily for the website.
    - A call to action button to prompt guest users to sign up to access full features of the site is provided right after all the stories
      and a clear sign up button is highlighted in Nav bar.

 **Registered user**

* As a registered user of Air Bubble, I want to be able to login to the site using my username and password.
  - Log in page is easily accessible from the navbar and allows registered users to easily log in to their account.
* As a registered user of Air Bubble, I want to be able to add my travel experience to contribute to the community.
  - When logged in, registered users are able to access Share your story - with two options to add new story or edit a old one.
* As a registered user of Air Bubble, I want to be able to see all my added stories on my profile and can edit or delete them
  - Logged in registered users can view all their added stories in their profile page. They can edit or delete them. 
    Clicking on edit post from share your story in Nav bar also takes user to profile page to edit or delete their posts.
* As a registered user of Air Bubble, I want to be able to confirm deletion before deleting my entries.
  - If users wish to delete the story they've added previously, they have to confirm deletion by clicking on Delete button again on a pop-up modal.
    This was designed to avoid accidental deletion.

 **Site owner / admin**

* As a site owner of Air Bubble, I want to be able to delete entries contributed by registered users if necessary.
  - The admin user is authorised to remove any content that is deemed irrelevant or inapropriate.

**[back to top](#testing)**

### Functionality Testing
___

 **Home Page**

  **Navigation Bar**

  - The bootstrap navbar is fixed and is visible across all pages and on all screen size devices. Navbar menu collapses into a hamburger menu on Tablets and smaller devices.
  - The sidenav, which was used in conjunction with the fullscreen navigation is working as desired and is visible on screen sizes
  - All the links on both, navbar and a sidenav were checked by clicking and are working as intended, allowing users to jump to the linked page.
  - The brand logo link was also tested by clicking and is working correctly, as it takes users back to the Home page from anywhere on the site.


  **Search box**
  
  The input field was tested by:
  * Entering airport codes and country names that exist in the stories and clicking the _Search button_ - the selected story or stories, in case if more than one is available, are displayed 
  * Typing words that are not in the website stories and clicking the Search button - nothing is displayed on the page.

  In both cases users see _search_ button that refreshes the page and displays all the stories contained in the website.
  * Clicking on the _Search button_ without entering any value - _Please fill in this field_ message is displayed, prompting users to enter a value. All above described features are working as intended.

  * Reset button is tested, by typing some text and checked if the page is reloaded by clicking and the reset button is fucntioning as intended.

  **Travel stories**
  
  Selected travel story cards were tested by:
  * clicking on read more button and to see if all the information can be read on a new page.
  * This step is repeated on all different devices and checked if rendered information is easy to read and neatly aligned.

**Call Out**
  
  Call out banner to sign up is tested by:
  * clicking on sign up button and to see if the sign up page is displayed


**Login Page**

* The page only appears when the user is not logged in.
* Verified, the Flash message always pops up when users successfully log in to the website. 
* Link below the login section was clicked to test and is functioning as it should, redirecting users to the _Sign Up_ page.
* Both username and password fields are tested with out an entry and user is prompted to enter the details
* In case of either wrong username or wrong password, a flash message is displayed to let the user know the details are wrong.

 **Sign Up Page**

* Sign Up page only appears when the user is not logged in.
* Flash message pops up to confirm the successul registration.
* The link below the sign up is fully functional, redirects users to the _Log In_ page.
* All the entries are tested without entering any details, and user is prompted to enter the details
* Email address is entered in wrong format and user is prompted to enter the right format
* Requirements of username and password are tested with wrong format entry( apart from numbers and letters) and user is 
  prompted to enter the right format
* successfull sign up takes the user to their profile page, and navbar is displayed with share my story and logout options.

 **Profile Page**

* Profile page is checked if the right username and right email address is displayed as entered by user
* Change password button is checked , if the password can be updated and flash message is displayed upon successful change
* Current password is wrongly entered to test if the user be given a message to enter the right password.
* After sharing a story, Profile page is visited to back to check if the user entered story is being displayed in the profile
* Checked if the user story in profile is coming with edit and delete options
* Edit button is checked if the page takes user to edit the information of their story.
* Delete button is tested if the confirm delete option (modal) is being displayed and the next selections on modal are working perfectly.
  Both the cancel and delete buttons are functioning as intended. Flash message is displayed upon successfull deletion


**Share your Story Page**

  New Post

* Share my story button is tested with out entry in any fields and checked if the user is prompted to fill the mandatory fields.
* Flash message is displayed upon successful entry of the story
* Home page is checked if the added story is being displayed with a read more button

  Edit post

* Edit post button from Navbar is tested to see if the user is taken to Profile page for editing their stories
* Edit button is tested and information is changed and submitted to check if the information is updated. Functioning as intended
* Flash message is displayed after the story is updated


**Log Out Page**

* The page is visible for logged in users only.
* The _Log Out_ link on the navbar (sidenav on smaller screens) is working as expected and logs users out of their account when clicked.
* Further tests verified that users are then redirected to the _Log In_ page where a flash message pops up to confirm they've been logged out. 


**Readmore Page**

* Readmore button is tested to see if the user is taken to read more page with full information
* Comments section is tested both by entering comments with out logged in user and with logged in user.
  comments are rendering as intended

**Admin user profile**

* Admin user is logged in and tested if the admin can be able to delete all the stories when read more button is used
* Flash message is displayed upon successfull deletion
* Checked and tested if all the comments made, have delete option visible to the admin.

**[back to top](#testing)**

### Defensive Design Testing
___
* **Registration attempt with an existing email address**

  Returns flash message "Email address already registered".
  ![Email address exists](static/assets/img/email_existing.jpg)

* **Registration attempt with an existing username**

  Returns flash message "Username already existing".
  ![Username exists](static/assets/img/username_existing.jpg)

* **Registration attempt with an wrong email format**

  prompts user to use the right format
  ![Email format wrong](static/assets/img/wrong_email.jpg)

* **Login attempt with an wrong username or password**

  Returns flash message "Incorrect username and/or password".
  ![Wrong entries](static/assets/img/wrong_details.jpg)

* **Add Story form validation**

  Prompts user to fill in mandatory fields.
  ![Form validation](static/assets/img/add_story_validation.jpg)

* **Current password mismatch while changing password**

  Returns flash message "Your current password does not match with our records".
  ![Current password mismatch](static/assets/img/current_password_mismatch.jpg)

* **Confirmation before deleting the story**

  Modal popup to let user confirm the deletion.
  ![Confirm Deletion](static/assets/img/delete_modal.jpg)

**[back to top](#testing)**

### Responsiveness

The responsiveness of the website was tested on all popular devices, including iPhone 5/SE Android Pixel 2, Samgung Galaxy S5, iPhone 6/7/8, iPad, iPad Pro, etc using [Responsinator](https://www.responsinator.com/), and Google Dev Tools Device Mode. Travel stories display on medium screens are adjusted after this test.

It was tested on physical devices including iPhone XR and iPad. All tests have shown that site is fully responsive and fits and adapts well to the different viewport size devices.

### Usability Testing

This website was tested for usability by my family and friends. Overlapping of test in forms is identified through this process on small screens and fixed later.
Later, They didn't experience any issues during the testing process and it was confirmed that the website was easy to use and navigate. They were able to intuitively use the interactive elements of the website, find the information they were looking for and easily understand the purpose of the website.


### Performance Testing

Performance testing was carried out using Lighthouse in Chrome Developer Tools. The tests had shown good performance and excellent accessibility and best practice results for desktop devices. 
Steps taken to improve performance for the mobile devices following the initial tests:
* Added meta description to the site to improve best practices

### Browser Compatibility Testing

Website is checked on different browsers, including Chrome, Safari, Firefox and Edge

**[back to top](#testing)**