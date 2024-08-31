# Pagination

This project is all about pagination. Pagination is a common feature in web applications that allows users to navigate through a large set of data by breaking it up into smaller chunks.

## Features
- Pagination of large data sets
- Customizable number of items per page
- Previous and Next buttons for easy navigation
- Page number input field for direct access to specific pages

## Usage
To use the pagination feature in your web application, simply include the Pagination script and stylesheet in your project and initialize it with the desired options. 

```javascript
const pagination = new Pagination({
    itemsPerPage: 10,
    totalItems: 100,
    currentPage: 1,
    container: document.querySelector('#paginationContainer')
});
```

## Contributing
Contributions are welcome! If you would like to improve or add new features to the Pagination project, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to reach out if you have any questions or need assistance with the Pagination project. Thank you for using Pagination!