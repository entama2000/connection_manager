# connection_manager

## API Endpoints Overview

### Accounts API

- **Login**
  - **URL:** `/accounts/login/`
  - **Method:** `POST`
  - **Description:** Authenticates the user and returns JWT access and refresh tokens.

- **Signup**
  - **URL:** `/accounts/signup/`
  - **Method:** `POST`
  - **Description:** Registers a new user. The request body must include `username` and `password`. Upon signup, JWT tokens are returned.

- **Logout**
  - **URL:** `/accounts/logout/`
  - **Method:** `POST`
  - **Description:** Allows an authenticated user to log out. It registers the provided refresh token into a blacklist.

- **Token Refresh**
  - **URL:** `/accounts/refresh/`
  - **Method:** `POST`
  - **Description:** When a valid refresh token is provided, a new access token is issued.

### Friends API

- **List & Create Friend**
  - **URL:** `/friends/`
  - **Methods:**
    - `GET`  
      - **Description:** Retrieves all friends associated with the currently logged-in user.
    - `POST`  
      - **Description:** Creates a new friend record. The request body must include at least `first_name` (required) and `last_name`. Other optional fields are `phone_number`, `platform` (e.g., "Twitter"), `birthday`, etc.

- **Friend Detail, Update & Delete**
  - **URL:** `/friends/<pk>/`
  - **Methods:**
    - `GET`  
      - **Description:** Retrieves the details of the friend identified by the provided primary key (pk).
    - `PUT`  
      - **Description:** Performs a full update of the friend record. The request must include all required fields.
    - `PATCH`  
      - **Description:** Performs a partial update, meaning only the fields specified in the request body will be updated.
    - `DELETE`  
      - **Description:** Deletes the friend record identified by the primary key.

## Example Requests

### Signup

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}' \
     http://<YOUR_DOMAIN>/accounts/signup/
```

### Login

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}' \
     http://<YOUR_DOMAIN>/accounts/login/
```

### Get Friends List

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     http://<YOUR_DOMAIN>/friends/
```

### Create a Friend

```bash
curl -X POST -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"first_name": "Taro", "last_name": "Yamada", "phone_number": "1234567890", "platform": "Twitter"}' \
     http://<YOUR_DOMAIN>/friends/
```

### Update a Friend (Full Update with PUT)

```bash
curl -X PUT -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"first_name": "Taro", "last_name": "Yamada", "phone_number": "9876543210", "platform": "Twitter"}' \
     http://<YOUR_DOMAIN>/friends/1/
```

### Partial Update a Friend (with PATCH)

```bash
curl -X PATCH -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"phone_number": "9999999999"}' \
     http://<YOUR_DOMAIN>/friends/1/
```

### Delete a Friend

```bash
curl -X DELETE -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     http://<YOUR_DOMAIN>/friends/1/
```

## Additional Notes

- **Authentication:**  
  All endpoints except for `/accounts/signup/` and `/accounts/login/` require JWT authentication. Ensure that your request headers include `Authorization: Bearer YOUR_ACCESS_TOKEN`.

- **Updating Records:**  
  A PUT request requires all essential fields (e.g., `first_name`, `last_name`) to be included in the request body for a full update. For partial updates, use the PATCH method.

- **Database Changes:**  
  After modifying the models, run the following commands to create and apply migrations:
  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```