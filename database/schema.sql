# MongoDB Collection Schemas for Meal Planning MVP

## Users
```json
{
  "_id": "ObjectId",
  "username": "string",
  "email": "string",
  "password": "string",
  "created_at": "Date",
  "updated_at": "Date"
}
```

## Meals
```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "date": "Date",
  "meal_type": "string", // e.g., Breakfast, Lunch, Dinner
  "recipes": ["ObjectId"] // Array of recipe IDs
}
```

## Recipes
```json
{
  "_id": "ObjectId",
  "name": "string",
  "ingredients": [
    {
      "name": "string",
      "quantity": "string"
    }
  ],
  "instructions": "string",
  "created_at": "Date",
  "updated_at": "Date"
}
```

## Shopping Lists
```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "date": "Date",
  "items": [
    {
      "name": "string",
      "quantity": "string"
    }
  ]
}
```

## Workflows
```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "steps": ["string"], // Array of step descriptions
  "created_at": "Date",
  "updated_at": "Date"
}
```
