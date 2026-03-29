# API Integration Documentation

This document provides guidelines for integrating with the Meal Planning MVP API.

## Authentication Endpoints
- **POST /auth/login**: Logs in a user and returns a token.
- **POST /auth/logout**: Logs out a user and invalidates the token.

## Meal Planning Endpoints
- **GET /meals**: Retrieves a list of meals for the authenticated user.
- **POST /meals**: Creates a new meal entry.
- **PUT /meals/{id}**: Updates a meal entry by ID.
- **DELETE /meals/{id}**: Deletes a meal entry by ID.

## Recipe Endpoints
- **GET /recipes**: Retrieves a list of available recipes.
- **GET /recipes/{id}**: Retrieves detailed information about a specific recipe.
- **POST /recipes**: Adds a new recipe.

## Shopping List Endpoints
- **GET /shopping-list**: Retrieves the shopping list for the authenticated user.
- **POST /shopping-list**: Adds items to the shopping list.
- **DELETE /shopping-list/{id}**: Removes items from the shopping list.

## Authentication Methods
- Use **Bearer Token** for authenticating API requests by including `Authorization: Bearer {token}` in the header.

## JavaScript/React Integration Examples
```javascript
const apiUrl = 'https://api.mealplanningmvp.com';
const token = 'YOUR_ACCESS_TOKEN';

const fetchMeals = async () => {
  const response = await fetch(`${apiUrl}/meals`, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  const meals = await response.json();
  return meals;
};
```

## Webhook Integration
- Set up webhooks to receive real-time updates about meal planning changes.
- **POST /webhooks**: Subscribe to events. 

## Rate Limiting
- APIs are rate limited to 100 requests per hour per user. Exceeding this limit will result in HTTP 429 status code.

## Error Handling
- Common errors include:
  - `400 Bad Request`: Invalid request format.
  - `401 Unauthorized`: Authentication failed.
  - `404 Not Found`: Resource not found.
- All errors will return a JSON object with an error message.

## Third-Party Service Integration Options
- Integration with popular nutrition databases and recipe services is available. Please refer to the service documentation for specific endpoints.

---

> **Note:** Please consider caching results to minimize API requests and improve performance.