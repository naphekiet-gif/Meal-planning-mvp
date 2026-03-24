// Categories used in the meal planning app
const CATEGORIES = [
    'Breakfast',
    'Lunch',
    'Dinner',
    'Snacks',
    'Desserts'
];

// Color codes for different categories
const CAT_COLORS = {
    'Breakfast': '#FFDDC1',
    'Lunch': '#FFABAB',
    'Dinner': '#FFC3A0',
    'Snacks': '#FF677D',
    'Desserts': '#D4A5A5'
};

// Common allergens
const COMMON_ALLERGENS = [
    'Peanuts',
    'Tree Nuts',
    'Dairy',
    'Eggs',
    'Gluten',
    'Soy'
];

// Common dietary restrictions
const COMMON_DIETARY = [
    'Vegetarian',
    'Vegan',
    'Paleo',
    'Keto',
    'Gluten-Free'
];

// Initial pantry ingredients
const INITIAL_PANTRY = [
    'Olive Oil',
    'Salt',
    'Pepper',
    'Garlic',
    'Onions',
    'Rice',
    'Pasta',
    'Canned Tomatoes',
    'Beans'
];

// Initial recipes for the app
const INITIAL_RECIPES = [
    {'name': 'Spaghetti', 'ingredients': ['Pasta', 'Tomato Sauce']},
    {'name': 'Salad', 'ingredients': ['Lettuce', 'Tomato', 'Cucumber']},
    {'name': 'Grilled Chicken', 'ingredients': ['Chicken', 'Garlic', 'Olive Oil']}
];

// Sample explore data
const SAMPLE_EXPLORE = [
    {'title': 'Healthy Breakfast Ideas', 'link': 'https://example.com/breakfast'},
    {'title': 'Quick Lunches', 'link': 'https://example.com/lunch'},
    {'title': 'Dinner Recipes', 'link': 'https://example.com/dinner'}
];

module.exports = { CATEGORIES, CAT_COLORS, COMMON_ALLERGENS, COMMON_DIETARY, INITIAL_PANTRY, INITIAL_RECIPES, SAMPLE_EXPLORE };