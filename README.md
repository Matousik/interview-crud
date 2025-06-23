# People Directory CRUD Application - Interview Task

## Task Description

You need to implement a complete CRUD (Create, Read, Update, Delete) application for managing people, let's call it e.g. People Directory. The application should allow users to:

- **Create** new people with name, email, and age
- **Read** all people and display them in a table
- **Update** existing persons information
- **Delete** a specific person

### Requirements

- Design an appropriate database schema for table People with following fields:
   - id, firstName, lastName, email, age
- First name, last name and email are required fields
- Email must be unique
- Age is optional
- Add tests for your operations

### As a follow-up

- **Filter** among existing people for name, email and age
   - Filter for first name and partial name, allow partial match
   - For age, allow also filtering by range
- **Validate** the form input. E.g. make email required and unique among people, allow adding only adults
- **Implement pagination**
- **Implement sorting**, e.g. by age, name, date the user has been added - you can create additional column for that with automatic filling
- **Make the interface responsive**, ideally keep mobile-first approach in mind

## Evaluation Criteria

- ✅ Database schema based on requirements
- ✅ All CRUD operations work correctly
- ✅ Clean and maintainable code
- ✅ Good user experience
- ✅ Proper error handling
- ✅ Responsive design
- ✅ Code organization and structure
- ✅ Good test coverage

## Additional information

We don't care how you'll implement this, just show us you can do it! Work just as how you normally would on the job - search online, go through documentation, use whichever code assist tools you want. We want to know that you know how stuff works and if you can get things done.

You have free will to choose the tech stack for this project. To ease your burden, you can find a few starter sekeletons for several frameworks in Python or Node.js that you can use.

Good luck!
