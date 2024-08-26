# [Flavor Hub](https://flavor-hub-c7318789b1c4.herokuapp.com/)

![flavor-hub](documentation/flavor-hub.png)

source: [Am I Responsive](https://ui.dev/amiresponsive?url=https://flavor-hub-c7318789b1c4.herokuapp.com/)

### Welcome to Flavor Hub
Our platform allows users to explore, search, and discover a wide variety of recipes. With a simple sign-up, you can add, edit, and share your own culinary creations, making Flavor Hub your go-to destination for all things delicious.

## User Experience(UX)
- ### User stories
    - #### New Site Users
        - As a new site user, I would like to see a clear logo and website name to remember the brand.
        - As a new site user, I would like to see a clear message about the web app’s purpose so that I can understand what the application is about.
        - As a new site user, I would like to see a navigation bar so I can navigate around the site.
        - As a new site user, I would like to easy sign up the website, so that I can access personalised features like adding and editing recipe.
        - As a new site user, I would like to have a search bar to search the recipe.
        - As a new site user, I would like to see social media icons so that I can reach out to other sources.


    - #### Returning Site Users
        - As a returning site user, I would like to log in securely, so I can manage my recipes.
        - As a returning site user, I would like to add a new recipe, so that I can share my favorite sidhes with others.
        - As a returning site user, I would like to edit my existing recipes, so that I can update or improve them over time.
        - As a returning site user, I would like to delete a recipe I've added, so that I can manage my recipe collection.
        - As a returning site user, I would like to mark some recipes as my favorites so that I can easily find them later.
        - As a returning site user, I would like to see a community of other cooks and food enthusiasts so that I can learn more and share my experiences.
        - As a returning site user, I would like to make posts in the community so that I can share my cooking experiences and tips.
        - As a returning site user, I would like to comment on others' posts in the community so that I can engage in discussions and exchange ideas.
        - As a returning site user, I would like to view all the recipes I have added on one page so that I can easily manage them.
        - As a returning site user, I would like to log out to keep my session secure when using shared devices.
        - As a returning site user, I would like to have access to a dedicated page for each recipe where I can view and add detailed information about that recipe.
        - As a returning site user, I would like to be able to edit information on each specific recipe page to keep it accurate and up-to-date.

    - #### Site Admin
        - As a site administrator, I would like to stay connected with users so that they can report any issues or provide feedback on user experience.
        - As a site administrator, I should be able to delete posts that violate community guidelines to ensure the site remains a safe and welcoming space.
        - As a site administrator, I should be able to view who created each post so that I can monitor content and user activity.
        - As a site administrator, I should be able to delete users who violate the rules to maintain a safe and respectful community.
        - As a site administrator, I need to manage and view user accounts effectively to maintain control over the user base and monitor activity.
        - As a site administrator, I should be able to direct users back to the homepage if they encounter a page that is not found (404 error).
        - As a site administrator, I should be able to redirect users to the homepage if they try to access a page that is forbidden (403 error).
        - As a site administrator, I should be able to handle internal server errors by redirecting users back to the homepage with an appropriate message (500 error).

## Design
- ### Typography
    - Google Fonts was used to import the fonts selected for this website. Imprima was chosen as the primary font for the entire site due to its clean and modern appearance, which ensures readability across all devices. Arimo was selected for the headings (h1-h6) to provide a distinct and professional look, adding emphasis and structure to the content. In case these fonts are not supported by the browser, a fallback to a generic sans-serif font was included to maintain consistency and readability.

- ### Colour Scheme
    I used [coolors.co](https://coolors.co/092b4a-0d3b66-fafafa-faf9f4-faf0ca-f4d35e-ee964b-ee7c1b-f95738) to generate the color palette for the website. Orange, blue, and their corresponding hues were selected for their association with energy and harmony, making them ideal for a website dedicated to recipes. These colors enhance the visual appeal and create a welcoming environment for users.
    ![color-frame](documentation/colour.png)



## Wireframes

I have use [Balsamiq](https://balsamiq.com/wireframes/) to design my site wireframes.

### Home Page

<details>
<summary> Click here to see Wireframe</summary>

  ![index](documentation/wireflame/index.png)

</details>

### Sign In Page

<details>
<summary> Click here to see Wireframe</summary>

  ![sign-in](documentation/wireflame/sign_in.png)
  
</details>

### Register Page

<details>
<summary> Click here to see Wireframe</summary>

  ![register](documentation/wireflame/register.png)
  
</details>

### Add Recipe Page

<details>
<summary> Click here to see Wireframe</summary>

  ![add-recipe](documentation/wireflame/add_recipe.png)
  
</details>

### Edit Recipe Page

<details>
<summary> Click here to see Wireframe</summary>

  ![edit-recipe](documentation/wireflame/edit_recipe.png)
  
</details>

### Recipe Page

<details>
<summary> Click here to see Wireframe</summary>

  ![recipe](documentation/wireflame/recipe.png)
  
</details>

### Profile Page

<details>
<summary> Click here to see Wireframe</summary>

  ![profile](documentation/wireflame/profile.png)
  
</details>

## Features

### Existing Features

  - #### Hero Image
    - Clearly communicates the purpose of the website to the user.

  - #### Welcome Text and Callout Message
    - A welcoming message that introduces the site name and invites users to explore the recipes.

  - #### Call-to-Action Button
    - A prominent button that guides users to take specific actions, simplifying navigation.
    ![callout](documentation/Feature/index/callout.png)

  - #### About Text
    - Provides an overview of the website's purpose.
    ![about](documentation/Feature/index/about.png)

  - #### Search Bar
    - Enables users to search for recipes by name, category, or cuisine.
    - Displays the number of posts matching the search query when successful.
    - Shows a message if no results are found, informing users that nothing matched their search term.
    ![search bar](documentation/Feature/index/search.png)
    ![no-results](documentation/Feature/index/no-results.png)

  - #### Card
    - Appears on both the Profile Page and the Home Page.
    - Features a hover effect that adds shadows to enhance visual appeal.
    - Displays images uploaded by users, along with the title and a brief description.
    - Includes two buttons for editing or deleting the post.
    ![card](documentation/Feature/index/card.png)
    ![card1](documentation/Feature/index/card1.png)

  - #### NavBar
    - Provides users with a clear and accessible pathway to navigate through the website:
    - Includes links to key sections like Home, Profile, Add Recipe, and more.
    - Adapts to different screen sizes, ensuring a seamless experience on both desktop and mobile devices.
    - Enables easy access to user-specific features, such as login, registration, and logout options.
    ![nav](documentation/Feature/index/nav.png)
    ![side-nav](documentation/Feature/index/side-nav.png)

  - #### Footer
    - Provides essential information and additional navigation options for users
    - About Us Text: Briefly describes the purpose and mission of Flavor Hub, offering users insight into the website's focus on culinary inspiration and community.
    - Quick Links: Offers easy access to important sections of the website, such as Home, Profile, and Add Recipe, ensuring users can quickly navigate to key areas.
    - Social Media Links: Connects users to Flavor Hub's social media profiles, allowing them to stay updated and engaged with the community on platforms like Facebook, Instagram, X and YouTube.
    ![footer](documentation/Feature/index/footer.png)

  - #### Registration Page
    - Enables users to securely create an account on Flavor Hub, allowing them to personalize their experience, save their favorite recipes, and contribute their own culinary creations.
    ![register](documentation/Feature/login-register/register.png)

  - #### Log In Page
    - Provides returning users with a secure way to access their accounts, manage their recipes, and engage with the community. Ensures that users can easily continue where they left off, whether adding new recipes or editing existing ones.
    ![login](documentation/Feature/login-register/login.png)
  
  - #### Contact Us
    - Provides users with a simple and convenient way to reach out to the Flavor Hub team for questions, feedback, or assistance.
    - When users contact the admin through the contact page, they receive an immediate auto-reply, confirming their message has been received.
    - This feature ensures users feel acknowledged and reassured that their inquiries are being addressed promptly.
    ![contact-us](documentation/Feature/login-register/contact.png)
    ![auto-reply](documentation/Feature/login-register/auto-reply.png)

  - #### Add Recipe Page
    - Allows users to contribute to the Flavor Hub community by adding their own recipes. Users can input ingredients, cooking steps, preparation time, and more to share their culinary creations with others.
    ![add-recipe](documentation/Feature/add-new-recipe/add-recipe.png)
    ![add-recipe2](documentation/Feature/add-new-recipe/add-recipe2.png)

  - #### Edit Recipe Page
    - Enables users to update or modify their previously submitted recipes. This feature ensures that users can keep their recipes accurate and up-to-date.
    - Includes a "Cancel" button that allows users to return to the home page without making any changes.
    ![edit-recipe](documentation/Feature/add-new-recipe/add-recipe.png)
    ![edit-recipe2](documentation/Feature/add-new-recipe/edit-recipe2.png)

  - #### Delete Recipe
    - Allows users to delete their recipes using a dedicated delete button.
    - After clicking the delete button, a confirmation alert prompts to confirm the deletion, helping to prevent accidental removals.
    ![delete-alert](documentation/Feature/add-new-recipe/delete-alert.png)


  - #### Recipe Page
    - Displays detailed information about each recipe, including ingredients, step-by-step cooking instructions, preparation time, and cooking time. This makes it easy for users to browse and follow the recipe.
    ![recipe](documentation/Feature/add-new-recipe/recipe.png)

  - #### Profile Page
    - Allows users to easily manage their recipes in one place.
    - Users can view, edit, or delete their submitted recipes directly from their profile page.
    ![profile](documentation/Feature/add-new-recipe/profile.png)

  - #### '404' Page
    - Informs users that the page they are trying to access cannot be found. This helps users understand they may have entered an incorrect URL or the page has been moved or deleted.
    ![404](documentation/Feature/error/404.png)

  - #### '403' Page
    - Alerts users that they do not have the necessary permissions to access the requested page. This helps maintain security by restricting access to unauthorized users.
    ![403](documentation/Feature/error/403.png)

  - #### '500' Page
    - Notifies users of an internal server error, indicating something went wrong on the server side. This ensures users are aware of the issue while the development team resolves it.
    ![500](documentation/Feature/error/500.png)

### Admin Features
  - #### Manage Categories
    - Add Category: Allows the admin to create new categories by clicking the "Add Category" button, enabling better organization of recipes.
    - Edit and Delete Categories: Displays a list of all existing categories, providing the admin with options to edit or delete them as needed for maintaining an organized structure.
    ![Manage Categories](documentation/Feature/admin/manage_categories.png)
    ![Edit Categories Page](documentation/Feature/admin/edit_category.png)

  - #### Manage Users
    - View Users: Enables the admin to view a list of all registered users on the platform, offering insight into the user base.
    - Delete Users: Provides the admin with the ability to delete users and all posts associated with them, ensuring control over the content and user management.
    ![Manage Users](documentation/Feature/admin/manage_user.png)


### Future Features
  - #### Favorites
    - Save Favorite Recipes: Users will be able to mark their favorite recipes and save them to their profiles for easy access, creating a personalized collection of go-to dishes.

  - #### Leave Comments
    - Comment and Rate Recipes: Users will have the ability to leave comments and rate recipes, fostering community interaction and providing feedback to recipe creators.
  
  - #### Blog Community
    - Community Blog: A blog section will be incorporated, allowing users to share their cooking experiences, tips, and stories, creating a vibrant community space for discussion and inspiration.



## Tools and Technologies Used
  - [Balsamiq](https://balsamiq.com/wireframes) - Used for creating wireframes.
  - [Git](https://git-scm.com) - Version control system to track code changes.
  - [GitHub](https://github.com) - Secure online platform for code storage and collaboration.
  - [Gitpod](https://gitpod.io) - Cloud-based IDE for development.
  - [HTML](https://en.wikipedia.org/wiki/HTML) - Markup language for the main site content.
  - [CSS](https://en.wikipedia.org/wiki/CSS) - Stylesheet language used for site design and layout.
  - [JavaScript](https://www.javascript.com) - Programming language used for user interaction on the site.
  - [jQuery](https://jquery.com) - JavaScript library used to simplify DOM manipulation and event handling.
  - [Python](https://www.python.org) - Back-end programming language used to build server-side logic.
  - [Flask](https://flask.palletsprojects.com) - Python web framework used to create the web application.
  - [MongoDB](https://www.mongodb.com) - Non-relational database used with Flask for data storage and management.
  - [Heroku](https://www.heroku.com) - Cloud platform used for hosting and deploying the back-end application.
  - [Materialize](https://materializeweb.com)  - Front-end framework for responsive design and pre-built components.
  - [Font Awesome](https://fontawesome.com) - Icon library used for scalable vector icons.
  - [Google Fonts](https://fonts.google.com/icons) - Source for web fonts and icons used across the site.
  - [ChatGPT](https://chat.openai.com) - AI tool used to assist in writing content.
  - [Email JS](https://www.emailjs.com/) - Service used to send automatic email replies to users after contact.
  - [fontjoy](https://fontjoy.com/) - Tool used for testing and choosing font combinations.
  - [Shopify](https://www.shopify.com/tools/logo-maker) - Tool used for generating the site's logo.
  - [Sweet Alert](https://sweetalert.js.org/guides/#installation) - Library used to style alerts on the site.
  - [Pinterest](https://www.pinterest.co.uk/) - Platform used to source inspiration and images.


## Database Design
  - ### Database Choice and Structure
    - **Flavor Hub** utilizes MongoDB, a non-relational database, for its flexibility and document-based data model. This structure is ideal for handling the varying attributes of recipes without requiring changes to the overall schema.
    - This flexible schema is advantageous as it allows for a variety of attributes to be stored, even as the data evolves over time.

  - ### Current Collections
     The database, named flavor_hub, currently contains the following collections:
      1. **users:** Stores user information and credentials.
      2. **recipes:** Contains detailed information about each recipe, such as ingredients, steps, and associated user ID.
      3. **categories:** Stores different categories under which recipes can be classified (e.g. Desserts, Main Course).

  - ### Future Database Collections
     In future iterations of Flavor Hub, we plan to introduce additional collections to enhance user interaction and personalization:
      1. **comments:** This collection will store user comments and ratings on recipes. It will be linked to both the `users` and `recipes` collections to manage feedback effectively.
      2. **favorites:** This collection will allow users to save their favorite recipes. It will link users to their selected recipes, providing a personalized experience.
  
    These future collections will be added to expand the functionality of Flavor Hub and enhance user engagement.
  
  - #### Database Schema Diagram
    I used [Lucidchart](https://www.lucidchart.com) to create the database schema diagram. This diagram visually represents the current collections, their relationships, and the fields within each collection.
    ![Database_scheme.png](documentation/Database_scheme.png)


## Agile Development Process
  - ### Trello
    use [trello](https://trello.com/) to plan the tasks
    ![trello](documentation/trello.png)

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found on [Heroku](https://flavor-hub-c7318789b1c4.herokuapp.com/).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the non-relational database.

To obtain your own MongoDB Database URI, sign up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com/), a Platform as a Service (PaaS), for cloud deployment. Follow these steps to deploy:

1. **Create a New Heroku App:**
   - Log in to your [Heroku Dashboard](https://dashboard.heroku.com).
   - Click "New" in the top-right corner and select "Create new app".
   - Enter a unique app name and choose a region (EU or USA), then click "Create App".

2. **Configure Environment Variables:**
   - Navigate to the "Settings" tab of your Heroku app.
   - Click "Reveal Config Vars" and set the following environment variables:

     | Key                        | Value                   |
     |----------------------------|-------------------------|
     | `IP`                        | `0.0.0.0`               |
     | `PORT`                      | `5000`                  |
     | `SECRET_KEY`                | Your own value          |
     | `MONGO_URI`                 | Your MongoDB connection string |
     | `MONGO_DBNAME`              | Your MongoDB database name |
     | `EMAIL_API`                 | Your EmailJS public key |

3. **Prepare Deployment Files:**
   - Ensure the following files are in the root directory of your project:

     - **`requirements.txt`**: Lists all required Python packages.
       ```bash
       pip3 freeze > requirements.txt
       ```

     - **`Procfile`**: Specifies the commands to run your application.
       ```bash
       echo web: python app.py > Procfile
       ```
       Replace `app.py` with the name of your primary Flask application file.

     - **`runtime.txt`**: Specifies the Python version.
       ```bash
       python-3.9.18
       ```

4. **Deploy Your Application:**
   - Log in to Heroku CLI:
     ```bash
     heroku login -i
     ```

   - Set the remote for Heroku:
     ```bash
     heroku git:remote -a app_name
     ```
     Replace `app_name` with your Heroku app name.

   - Push your code to Heroku:
     ```bash
     git push heroku main
     ```

   - Open your application in a browser:
     ```bash
     heroku open
     ```

### EmailJS Integration

To configure EmailJS for sending automatic replies:

1. **Sign Up:**
   - Create an account on [EmailJS](https://www.emailjs.com/).

2. **Create Email Service:**
   - Set up an email service in your EmailJS dashboard.

3. **Install EmailJS Library:**
   - Include the EmailJS script in your HTML or install it via npm:
     ```bash
     npm install --save @emailjs/browser
     ```
   - Or with yarn:
     ```bash
     yarn add @emailjs/browser
     ```

4. **Add EmailJS Script to Your Project:**
   - Include the following script in your HTML file:
     ```html
     <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
     <script type="text/javascript">
       (function(){
           emailjs.init({
             publicKey: "YOUR_PUBLIC_KEY",
           });
       })();
     </script>
     ```

5. **Create and Use Email Templates:**
   - Set up email templates in the EmailJS dashboard.
   - Use the following code to send emails:
     ```javascript
     emailjs.send(serviceID, templateID, templateParams, options);
     ```

### Local Development

To run the project locally:

1. **Clone the Repository:**
   - Clone the repository:
     ```bash
     git clone https://github.com/Lauren21717/flavor-hub.git
     ```

2. **Install Dependencies:**
   - Install the required packages:
     ```bash
     pip3 install -r requirements.txt
     ```

3. **Create a Local `env.py` File:**
   - Create a file named `env.py` with environment variables:
     ```python
     import os
     os.environ.setdefault("IP", "0.0.0.0")
     os.environ.setdefault("PORT", "5000")
     os.environ.setdefault("SECRET_KEY", "your_value")
     os.environ.setdefault("MONGO_DBNAME", "your_db_name")
     os.environ.setdefault("MONGO_URI", "your_mongo_uri")
     os.environ.setdefault("EMAIL_API", "your_email_api_key")
     os.environ.setdefault("DEBUG", "True")
     os.environ.setdefault("DEVELOPMENT", "True")
     ```

4. **Run the Application:**
   - Start the Flask application:
     ```bash
     python app.py
     ```

   - Access the application at `http://localhost:5000`.

### Cloning and Forking

#### Cloning

1. Go to the GitHub repository.
2. Click on the "Code" button and copy the URL.
3. Open your terminal and run:
   ```bash
   git clone https://github.com/Lauren21717/flavor-hub.git

#### Forking

By forking a GitHub repository, you create a personal copy of the original repository under your own GitHub account. This allows you to view and modify the code without affecting the original repository.

To fork this repository, follow these steps:

1. Log in to GitHub and navigate to the [GitHub Repository](https://github.com/Lauren21717/flavor-hub).
2. At the top-right corner of the repository page, just above the "Settings" button, click the "Fork" button.
3. After clicking the "Fork" button, a copy of the repository will be created under your GitHub account.

You can now work on your own copy of the repository, make changes, and propose improvements through pull requests if desired.

## Credits

- [Good Food](https://www.bbcgoodfood.com/) - Recipe content and food pictures.
- [W3Schools](https://www.w3schools.com/) - Function reference and examples.
- [Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/) - Jinja2 syntax for templates.
- [SweetAlert](https://sweetalert.js.org/guides/) - Styling flash messages on the page.
- [Pinterest](https://www.pinterest.co.uk/) - Images for the hero section.
- [Google](https://www.realsimple.com/thmb/bKxH2p6M6cvQWsvNu02PFdxmjfg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/How-to-organize-recipes-2000-c5bb82544cb643a0915be5841fb037e0.jpg) - Images for the about section.
- [Materialize CSS](https://materializecss.com/footer.html) - Footer design.
- [Shopify](https://www.shopify.com/tools/logo-maker) - Logo creation.
- [ChatGPT](https://chatgpt.com/) - Content assistance.
