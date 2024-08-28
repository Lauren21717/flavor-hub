## Code Validation

### HTML Validation
I have used the recommended [W3C HTML Validator](https://validator.w3.org) to validate all of my HTML files. Below are the results for each HTML page:

| HTML File | Validator Link | Screenshot | Notes |
| --- | --- | --- | --- |
| `index.html` | [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fflavor-hub-c7318789b1c4.herokuapp.com%2Findex) | ![Index Validation](documentation/html-validator/indexw3c.png) | No errors found |
| `register.html` | [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fflavor-hub-c7318789b1c4.herokuapp.com%2Fregister) | ![Register Validation](documentation/html-validator/registerw3c.png) | No errors found |
| `login.html` | [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fflavor-hub-c7318789b1c4.herokuapp.com%2Flogin) | ![Login Validation](documentation/html-validator/loginw3c.png) | No errors found |
| `contact.html` | [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fflavor-hub-c7318789b1c4.herokuapp.com%2Fcontact) | ![Contact Validation](documentation/html-validator/contactw3c.png) | No errors found |
| `recipe.html` | [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fflavor-hub-c7318789b1c4.herokuapp.com%2Frecipe%2F66a7e0fbc693449982dd3934) | ![Recipe Validation](documentation/html-validator/recipew3c.png) | No errors found |
| `profile.html` | N/A | ![Profile Validation](documentation/html-validator/profilew3c.png) | No errors found |
| `add_recipe.html` | N/A | ![Add Recipe Validation](documentation/html-validator/add-recipew3c.png) | No errors found |
| `edit_recipe.html` | N/A | ![Edit Recipe Validation](documentation/html-validator/edit-recipew3c.png) | No errors found |
| `add_category.html` | N/A | ![Add Category Validation](documentation/html-validator/add-categoryw3c.png) | No errors found |
| `edit_category.html` | N/A | ![Edit Category Validation](documentation/html-validator/edit-categoryw3c.png) | No errors found |
| `admin_dashboard.html` | N/A | ![Admin Dashboard Validation](documentation/html-validator/admin-dashboardw3c.png) | No errors found |
| `403.html` | N/A | ![403 Error Page Validation](documentation/html-validator/403w3c.png) | No errors found |
| `404.html` | N/A | ![404 Error Page Validation](documentation/html-validator/404w3c.png) | No errors found |
| `500.html` | N/A | ![500 Error Page Validation](documentation/html-validator/500w3c.png) | No errors found |

### CSS Validation

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files. Below are the results:

| File | Screenshot | Notes |
| --- | --- | --- |
| `style.css` | ![CSS Validation](documentation/validation/css-valida.png) | No errors found |

### JavaScript Validation

I have used [JSHint](https://jshint.com/) to validate all of my JavaScript files, configured to allow ES6 syntax. Below are the details:

| File | Screenshot | Notes |
| --- | --- | --- |
| `script.js` | ![JS Validation](documentation/validation/script-valida.png) | ES6 syntax validated, no critical errors found |
| `email.js` | ![JS Validation](documentation/validation/emailjs-validate.png) | ES6 syntax validated, no critical errors found |

### Python Validation

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| `app.py` | [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Lauren21717/flavor-hub/main/app.py) | ![screenshot](documentation/validation/python-validate.png) | No issues |
## Browser Compatibility

| Browser Tested | Intended Appearance | Intended Responsiveness |
| --- | --- | --- |
| Chrome | Good  | Good |
| Firefox | Good | Good |
| Safari  | Good | Good |

## Compatibility Testing

To ensure that the website is functional and visually consistent across various platforms, the site was tested on different devices (e.g., desktops, laptops, tablets, smartphones) and operating systems (e.g., Windows, macOS, iOS, Android).

- **Results**: The Home page displays correctly on desktops, laptops, and tablets. However, on smartphones, buttons on the Login, Register, and Contact pages were not centered on small screens.

### Page Alignment Issues and Fixes

| Page | Before | After |
| --- | --- | --- |
| `login.html` | ![login](documentation/compatibility/login-align.png) | ![login-fix](documentation/compatibility/login-align-fix.png) |
| `register.html`| ![register](documentation/compatibility/register-align.png) | ![register-fix](documentation/compatibility/register-align-fix.png) |
| `contact.html` | ![contact](documentation/compatibility/contact-align.png) | ![contact-fix](documentation/compatibility/contact-align-fix.png) |

### Device Responsiveness

| Device Tested | Site Responsive >= 700px | Site Responsive < 600px | Renders as Expected |
| --- | --- | --- | --- |
| Smartphones | N/A | Good | Good |
| Tablets | Good | N/A | Good |
| Laptops | Good | N/A | Good |
| Desktops | Good | N/A | Good |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop |
| --- | --- | --- |
| `index.html` | ![index mobile](documentation/lighthouse/index-mobile-lh.png) | ![index desktop](documentation/lighthouse/index-des-lh.png) |
| `register.html` | ![register mobile](documentation/lighthouse/reg-mob-lh.png) | ![register desktop](documentation/lighthouse/reg-des-lh.png) |
| `contact.html` | ![contact mobile](documentation/lighthouse/contact-mob-lh.png) | ![contact desktop](documentation/lighthouse/contact-des-lh.png) |
| `profile.html` | ![profile mobile](documentation/lighthouse/profile-mob-lh.png) | ![profile desktop](documentation/lighthouse/profile-des-lh.png) |
| `add_recipe.html` | ![add recipe mobile](documentation/lighthouse/add_rec-mob-lh.png) | ![add recipe desktop](documentation/lighthouse/add_rec-des-lh.png) |
| `edit_recipe.html` | ![edit recipe mobile](documentation/lighthouse/edit_res-mob-lh.png) | ![edit recipe desktop](documentation/lighthouse/edit_res-des-lh.png) |
| `login.html` | ![login mobile](documentation/lighthouse/login-mob-lh.png) | ![login desktop](documentation/lighthouse/login-des-lh.png) |
| `recipe.html` | ![recipe mobile](documentation/lighthouse/recipe-mobile-lh.png) | ![recipe desktop](documentation/lighthouse/recipe-des-lh.png) |
| `admin_dashboard.html` | ![admin mobile](documentation/lighthouse/admin-mob-lh.png) | ![admin desktop](documentation/lighthouse/admin-des-lh.png) |
| `add_category.html` | ![add category mobile](documentation/lighthouse/add_cat-mob-lh.png) | ![add category desktop](documentation/lighthouse/add_cat-des-lh.png) |
| `edit_category.html` | ![edit category mobile](documentation/lighthouse/edit_cat-mob-lh.png) | ![edit category desktop](documentation/lighthouse/edit_cat-des-lh.png) |


## User Story Testing

### New Site 

| User Story | Screenshot |
| --- | --- |
| **As a new site user, I would like to see a clear logo and website name to remember the brand.** | ![Screenshot of the homepage with a visible logo and website name](documentation/user-story/new-user/logo.png) |
| **As a new site user, I would like to see a clear message about the web app’s purpose so that I can understand what the application is about.** | ![Screenshot showing the clear message about the web app's purpose](documentation/user-story/new-user/about.png) |
| **As a new site user, I would like to see a navigation bar so I can navigate around the site.** | ![Screenshot of the navigation bar](documentation/user-story/new-user/nav.png) |
| **As a new site user, I would like to easily sign up on the website, so that I can access personalized features like adding and editing recipes.** | ![Screenshot of the sign-up page or form](documentation/user-story/new-user/register.png) |
| **As a new site user, I would like to have a search bar to search for recipes.** | ![Screenshot of the search bar in use](documentation/user-story/new-user/search.png) |
| **As a new site user, I would like to see social media icons so that I can reach out to other sources.** | ![Screenshot of social media icons](documentation/user-story/new-user/social-icon.png) |

## Returning Site Users

| User Story | Screenshot |
| --- | --- |
| **As a returning site user, I would like to log in securely, so I can manage my recipes.** | ![Screenshot of the login page](documentation/user-story/returning-user/login.png) |
| **As a returning site user, I would like to add a new recipe, so that I can share my favorite dishes with others.** | ![Screenshot of the add recipe page](documentation/user-story/returning-user/add-recipe.png) |
| **As a returning site user, I would like to edit my existing recipes, so that I can update or improve them over time.** | ![Screenshot of the edit recipe functionality](documentation/user-story/returning-user/edit.png) |
| **As a returning site user, I would like to delete a recipe I've added, so that I can manage my recipe collection.** | ![Screenshot of the delete recipe option](documentation/user-story/returning-user/delete.png) |
| **As a returning site user, I would like to mark some recipes as my favorites so that I can easily find them later.** | Future Feature |
| **As a returning site user, I would like to see a community of other cooks and food enthusiasts so that I can learn more and share my experiences.** | Future Feature |
| **As a returning site user, I would like to make posts in the community so that I can share my cooking experiences and tips.** | Future Feature |
| **As a returning site user, I would like to comment on others' posts in the community so that I can engage in discussions and exchange ideas.** | Future Feature |
| **As a returning site user, I would like to view all the recipes I have added on one page so that I can easily manage them.** | ![Screenshot of the user's recipe list](documentation/user-story/returning-user/profile.png) |
| **As a returning site user, I would like to log out to keep my session secure when using shared devices.** | ![Screenshot of the logout option](documentation/user-story/returning-user/log-out.png) |
| **As a returning site user, I would like to have access to a dedicated page for each recipe where I can view and add detailed information about that recipe.** | ![Screenshot of a recipe's detailed page](documentation/user-story/returning-user/recipe.png) |
| **As a returning site user, I would like to be able to edit information on each specific recipe page to keep it accurate and up-to-date.** | ![Screenshot of the recipe edit page](documentation/user-story/returning-user/edit-btn.png) |

## Site Admin

| User Story | Screenshot |
| --- | --- |
| **As a site administrator, I would like to stay connected with users so that they can report any issues or provide feedback on user experience.** | ![Screenshot of the contact form or feedback section](documentation/user-story/admin/contact_us.png) |
| **As a site administrator, I should be able to delete posts that violate community guidelines to ensure the site remains a safe and welcoming space.** | Future Feature |
| **As a site administrator, I should be able to view who created each post so that I can monitor content and user activity.** | Future Feature |
| **As a site administrator, I should be able to delete users who violate the rules to maintain a safe and respectful community.** | ![Screenshot of the delete user functionality](documentation/user-story/admin/delete_user.png) |
| **As a site administrator, I need to manage and view user accounts effectively to maintain control over the user base and monitor activity.** | ![Screenshot of the user management page](documentation/user-story/admin/manage-user.png) |
| **As a site administrator, I should be able to direct users back to the homepage if they encounter a page that is not found (404 error).** | ![Screenshot of the 404 error page](documentation/user-story/admin/404.png) |
| **As a site administrator, I should be able to redirect users to the homepage if they try to access a page that is forbidden (403 error).** | ![Screenshot of the 403 error page](documentation/user-story/admin/403.png) |
| **As a site administrator, I should be able to handle internal server errors by redirecting users back to the homepage with an appropriate message (500 error).** | ![Screenshot of the 500 error page](documentation/user-story/admin/500.png) |

## Defensive Programming

To ensure Flavor Hub's security, stability, and user-friendliness, several defensive programming techniques have been implemented:

1. Input Validation:
   - All user inputs are validated on both the client and server sides to prevent submission of malformed data.
   - Example: Recipe ingredients and steps are checked for minimum and maximum lengths to ensure proper content.

2. Authentication and Authorization:
   - User authentication is required to access specific features, such as adding or editing recipes.
   - Users are restricted to editing or deleting only their own recipes, ensuring data integrity and security.

3. Error Handling:
   - `Try-except` blocks are utilized to gracefully handle potential errors, preventing application crashes.
   - Custom error pages (404, 403, 500) provide clear and user-friendly messages to guide users when something goes wrong.

4. Confirmation:
   - Before any recipe deletion, a confirmation modal is displayed to the user to prevent accidental deletions.

5. Search Functionality:
   - The search bar does not accept empty input submissions.
   - Form validation prevents submission without input, and an appropriate error message is displayed to the user.

6. User Authentication Redirects:
   - Users attempting to access the dashboard without logging in are automatically redirected to an error page, maintaining the security of user data.


## Bugs

- **When adding a new recipe, the steps after step one won’t be inserted into the database.**

    - To address this issue, I double-checked my `script.js` and found a typo in the `name` attribute of the stepTextarea.

        From:

        ```javascript
        name: 'preparation_steps',
        ```

        To:

        ```javascript
        let stepTextarea = $('<textarea>', {
            id: 'step_' + stepCount,
            name: 'preparation_step',
            class: 'materialize-textarea',
            minlength: '5',
            maxlength: '200',
            required: true
        });
        ```

- **Time input field can be negative**  
  ![Time input field error](documentation/bugs/time-nav.png)
    - To fix this bug, I set `min="1"` on both `add_recipe.html` and `edit_recipe.html`, preventing negative numbers in the input field.
    ![Time input field error fixed](documentation/bugs/time-nav-fixed.png)

- **Ingredients inputs overlap with the label**  
  ![Ingredients input field](documentation/bugs/ing_label.png)
    - To fix this bug, I refactored the `input:text` to `textarea`.
    ![Ingredients input field fixed](documentation/bugs/ing_label_fixed.png)

- **Adding more ingredients input fields doesn’t allow typing sometimes**  
  ![Ingredients additional input field](documentation/bugs/ing-int.png)
    - To fix this bug, I refactored the `input:text` to `textarea`.
    ![Ingredients additional input field fixed](documentation/bugs/ing-int-fixed.png)

- **Unable to type "Thai" in the cuisine input field**  
  ![Cuisine](documentation/bugs/cusine_min.png)
    - To fix this issue, I adjusted the `minlength` attribute from 5 to 3 in both `add_recipe.html` and `edit_recipe.html`.

    From:

    ```html
    <input id="cuisine" name="cuisine" minlength="5" maxlength="50" type="text" class="validate" placeholder="Optional">
    ```

    To:

    ```html
    <input id="cuisine" name="cuisine" minlength="3" maxlength="50" type="text" class="validate" placeholder="Optional">
    ```

    ![Cuisine fixed](documentation/bugs/cusine_min_fixed.png)

- **In `admin_dashboard`, the edit category function is not working**

    - I discovered the issue was due to the `url_for` in `edit_category.html`'s cancel button.
    - To fix the bug, I changed `{{ url_for('get_categories') }}` to `{{ url_for('admin_dashboard') }}`.

    From:  
    ![Edit category](documentation/bugs/editcat-bug.png)  
    To:  
    ![Edit category fixed](documentation/bugs/editcat-bug-fixed.png)
