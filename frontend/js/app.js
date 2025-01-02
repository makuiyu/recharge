
document.addEventListener('DOMContentLoaded', function () {
    const API_BASE_URL = window.API_BASE_URL || 'localhost:30000';
    const USER_BASE_URL = window.USER_BASE_URL || 'user-service:5001';
    const ORDER_BASE_URL = window.ORDER_BASE_URL || 'order-service:5002';

    const mainContent = document.getElementById('main-content');

    document.getElementById('nav-users').addEventListener('click', loadUsers);
    document.getElementById('nav-orders').addEventListener('click', loadOrders);
    document.getElementById('nav-create-user').addEventListener('click', showCreateUserForm);
    document.getElementById('nav-create-order').addEventListener('click', showCreateOrderForm);

    function loadUsers() {
        axios.get(`http://${API_BASE_URL}/api/${USER_BASE_URL}/users`)
            .then(response => {
                const users = response.data;
                // let userList = '<h3>User List</h3><ul class="list-group">';
                // users.forEach(user => {
                //     userList += `<li class="list-group-item">${user.name} (${user.email})</li>`;
                // });
                // userList += '</ul>';
                let userList = '<h3>User List</h3>';
                userList += '<table class="table table-striped">';
                userList += '<thead>';
                userList += '<tr>';
                userList += '<th>#</th>';
                userList += '<th>Name</th>';
                userList += '<th>Email</th>';
                userList += '<th>Actions</th>';
                userList += '</tr>';
                userList += '</thead>';
                userList += '<tbody>';
                users.forEach(user => {
                    userList += `<tr class="align-middle">`;
                    userList += `<td>${user.id}</td>`;
                    userList += `<td>${user.name}</td>`;
                    userList += `<td>${user.email}</td>`;
                    userList += `<td>`;
                    userList += `<button class="btn btn-warning btn-sm">Edit</button>`;
                    userList += `<button class="btn btn-danger btn-sm ms-2">Delete</button>`;
                    userList += `</td>`;
                    userList += `</tr>`;
                });
                userList += '</tbody>';
                userList += '</tr>';
                userList += '</thead>';
                userList += '</table>';
                mainContent.innerHTML = userList;
            })
            .catch(error => {
                mainContent.innerHTML = '<p class="text-danger">Failed to load users</p>';
            });
    }

    function loadOrders() {
        axios.get(`http://${API_BASE_URL}/api/${ORDER_BASE_URL}/orders`)
            .then(response => {
                const orders = response.data;
                // let orderList = '<h3>Order List</h3><ul class="list-group">';
                // orders.forEach(order => {
                //     orderList += `<li class="list-group-item">Order ID: ${order.id}, User ID: ${order.user_id}, Status: ${order.status}</li>`;
                // });
                // orderList += '</ul>';
                let orderList = '<h3>Order List</h3>';
                orderList += '<table class="table table-striped">';
                orderList += '<thead>';
                orderList += '<tr>';
                orderList += '<th>#</th>';
                orderList += '<th>Order ID</th>';
                orderList += '<th>User ID</th>';
                orderList += '<th>Status</th>';
                orderList += '<th>Actions</th>';
                orderList += '</tr>';
                orderList += '</thead>';
                orderList += '<tbody>';
                orders.forEach(order => {
                    orderList += `<tr class="align-middle">`;
                    orderList += `<td>${order.id}</td>`;
                    orderList += `<td>${order.id}</td>`;
                    orderList += `<td>${order.user_id}</td>`;
                    orderList += `<td>${order.status}</td>`;
                    orderList += `<td>`;
                    orderList += `<button class="btn btn-warning btn-sm">Edit</button>`;
                    orderList += `<button class="btn btn-danger btn-sm ms-2">Delete</button>`;
                    orderList += `</td>`;
                    orderList += `</tr>`;
                });
                orderList += '</tbody>';
                orderList += '</tr>';
                orderList += '</thead>';
                orderList += '</table>';
                mainContent.innerHTML = orderList;
            })
            .catch(error => {
                mainContent.innerHTML = '<p class="text-danger">Failed to load orders</p>';
            });
    }

    function showCreateUserForm() {
        mainContent.innerHTML = `
            <h3>Create New User</h3>
            <form id="create-user-form">
                <div class="mb-3">
                    <label for="userName" class="form-label">Name</label>
                    <input type="text" class="form-control" id="userName" required>
                </div>
                <div class="mb-3">
                    <label for="userEmail" class="form-label">Email</label>
                    <input type="email" class="form-control" id="userEmail" required>
                </div>
                <button type="submit" class="btn btn-primary">Create User</button>
            </form>
        `;

        document.getElementById('create-user-form').addEventListener('submit', function (event) {
            event.preventDefault();
            const name = document.getElementById('userName').value;
            const email = document.getElementById('userEmail').value;

            axios.post(`http://${API_BASE_URL}/api/${USER_BASE_URL}/users`, { name, email })
                .then(response => {
                    alert('User created successfully!');
                    loadUsers();
                })
                .catch(error => {
                    alert('Failed to create user');
                });
        });
    }

    function showCreateOrderForm() {
        mainContent.innerHTML = `
            <h3>Create New Order</h3>
            <form id="create-order-form">
                <div class="mb-3">
                    <label for="userId" class="form-label">User ID</label>
                    <input type="number" class="form-control" id="userId" required>
                </div>
                <button type="submit" class="btn btn-primary">Create Order</button>
            </form>
        `;

        document.getElementById('create-order-form').addEventListener('submit', function (event) {
            event.preventDefault();
            const userId = document.getElementById('userId').value;

            axios.post(`http://${API_BASE_URL}/api/${ORDER_BASE_URL}/orders`, { user_id: userId })
                .then(response => {
                    alert('Order created successfully!');
                    loadOrders();
                })
                .catch(error => {
                    alert('Failed to create order');
                });
        });
    }
});