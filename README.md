# Grazioso Salvare Animal Shelter Dashboard

A full-stack web application for managing and visualizing animal shelter data to identify rescue dog training candidates. Built with Python, MongoDB, and Plotly Dash to provide interactive data exploration, filtering, and geolocation capabilities.

## Project Overview

This application provides a comprehensive dashboard interface for Grazioso Salvare, an international rescue animal training company, enabling users to:
- View and filter animal shelter outcome data from Austin-area shelters
- Identify dogs suitable for specific rescue training programs (Water, Mountain/Wilderness, Disaster/Individual Tracking)
- Visualize breed distribution through interactive pie charts
- Explore animal locations via geolocation mapping
- Perform CRUD operations on the shelter database

## Dashboard Demo

[![Dashboard Demo](https://img.youtube.com/vi/OsMyzGyEvUA/0.jpg)](https://youtu.be/OsMyzGyEvUA)

## Tech Stack

- **Backend:** Python 3.9+, MongoDB 5.0+
- **Frontend Framework:** Plotly Dash 2.x, Dash Bootstrap Components
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly Express, Dash Leaflet
- **Database Driver:** PyMongo
- **Styling:** Bootstrap (UNITED theme)

## Architecture

The application follows the **MVC (Model-View-Controller)** design pattern:

- **Model:** MongoDB database (`AAC.animals` collection) with custom Python CRUD module for data operations
- **View:** Dash components including interactive data tables, pie charts, and Leaflet maps
- **Controller:** Python callback functions managing real-time component interactions and data flow

### Why This Tech Stack?

**MongoDB**
- Flexible NoSQL schema accommodates varying animal data structures
- Built-in geospatial indexing and query support for location-based features
- Scalable architecture supports growing shelter data
- Document model aligns naturally with shelter record structure

**Plotly Dash**
- Python-native framework eliminates need for separate JavaScript development
- Reactive components enable real-time dashboard updates
- Built-in callback system simplifies complex user interactions
- Rapid prototyping accelerates development cycle

**PyMongo**
- Official MongoDB Python driver with robust error handling
- Connection pooling for improved performance
- Well-documented API with active community support
- Seamless integration with Pandas for data analysis

**Dash Bootstrap Components**
- Professional UI components without custom CSS overhead
- Responsive grid system for mobile compatibility
- Consistent theming across application
- Accessibility features built-in

## Features

### CRUD Operations Module (`animal_shelter.py`)

Custom Python class providing full database operations:

**Create**
- Insert new animal records into MongoDB
- Returns acknowledgment status
- Input validation and error handling

**Read**
- Flexible query interface supporting MongoDB query syntax
- Returns cursor results as Python list
- Handles empty results gracefully

**Update**
- Bulk update operations with `$set` operator
- Returns count of modified documents
- Supports complex query filters

**Delete**
- Remove documents matching query criteria
- Returns count of deleted documents
- Prevents accidental data loss with required query parameter

**Connection Management**
- Environment variable configuration for secure credential storage
- Automatic connection initialization
- Manual close method for cleanup

### Interactive Dashboard

**Welcome Section**
- Branded header with Grazioso Salvare logo
- Mission statement and usage instructions
- Responsive card layout with professional styling

**Data Table**
- Displays all animal records with sortable columns
- Pagination (10 records per page)
- Single-row selection for detail viewing
- Column headers auto-formatted from snake_case to Title Case
- Horizontal scroll for overflow data
- Custom styling matching brand colors

**Filter System**
- Dropdown menu with four filter options:
  - **Water Rescue:** Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland (Intact Female, 26-156 weeks)
  - **Mountain/Wilderness Rescue:** German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, Rottweiler (Intact Male, 26-156 weeks)
  - **Disaster/Individual Tracking:** Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, Rottweiler (Intact Male, 20-300 weeks)
  - **Reset:** Returns to unfiltered view
- Real-time table updates on filter selection
- Automatic first-row selection after filtering

**Visualization Charts**
- Dropdown selector to choose between two chart types:
  - **Breed Distribution:** Interactive pie chart showing top 8 breeds in filtered dataset
  - **Age Distribution:** Bar chart showing animals grouped by age ranges
- Custom hover tooltips with detailed data
- White borders for visual clarity
- Responsive to filter changes

**Geolocation Map**
- Interactive Leaflet map centered on selected animal's location
- Marker shows animal position in Austin, TX area
- Tooltip displays breed on hover
- Popup shows animal name on click
- Zoom level 10 for neighborhood-scale view
- Dynamic centering based on selected record

**CSV Export**
- Custom "Export to CSV" button in filter card
- Exports currently filtered/viewed table data
- Maintains data integrity with proper index handling
- Downloads as `shelter_data.csv`
- Implemented via custom callback for consistent styling (vs built-in DataTable export)

### Query Implementation

Pre-built MongoDB queries filter animals based on rescue type criteria:

```python
# Water Rescue Example
{
    'breed': {'$in': ['Labrador Retriever Mix', 'Chesapeake Bay Retriever', 'Newfoundland']},
    'sex_upon_outcome': 'Intact Female',
    'age_upon_outcome_in_weeks': {'$gte': 26, '$lte': 156}
}
```

Each query considers:
- Preferred breed list per rescue type
- Sex requirements (Intact Male/Female)
- Training age windows in weeks
- Compound conditions with MongoDB operators

## Project Structure

```
GraziosoSilvare/
├── venv/                              # Virtual environment (not in repo)
├── .env                               # Environment variables (not in repo)
├── .gitignore                         # Git ignore configuration
├── requirements.txt                   # Python dependencies
├── animal_shelter.py                  # CRUD module for MongoDB operations
├── dashboard.py                       # Main dashboard application
├── Grazioso Salvare Logo.png          # Brand logo image
├── README.md                          # This file
├── STYLE_GUIDE.md                     # Frontend design documentation
└── tests/
    └── test_crud.ipynb                # CRUD module test suite
```

## Database Schema

**Collection:** `AAC.animals`

**Key Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | MongoDB unique identifier |
| `animal_id` | String | Shelter's animal ID (e.g., A721199) |
| `animal_type` | String | Species (Dog, Cat, Bird, etc.) |
| `breed` | String | Specific breed or mix |
| `name` | String | Animal's name |
| `age_upon_outcome_in_weeks` | Integer | Age in weeks at outcome |
| `sex_upon_outcome` | String | Sex classification (Intact Male, Intact Female, etc.) |
| `outcome_type` | String | Outcome category (Adoption, Transfer, Return to Owner, etc.) |
| `location_lat` | Float | Latitude coordinate for shelter location |
| `location_long` | Float | Longitude coordinate for shelter location |
| `date_of_birth` | String | Birth date (YYYY-MM-DD format) |
| `datetime` | String | Outcome datetime timestamp |
| `color` | String | Animal's color description |

**Index Considerations:**
- Primary index on `_id` (automatic)
- Recommended: Compound index on `breed`, `sex_upon_outcome`, `age_upon_outcome_in_weeks` for filter performance
- Geospatial index on `location_lat` and `location_long` for map queries

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- MongoDB 5.0 or higher
- pip package manager
- 10,000+ records from Austin Animal Center Outcomes dataset

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/sldowd/grazioso-salvare-dashboard.git
cd grazioso-salvare-dashboard
```

**2. Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**Required packages:**
```
dash==2.18.2
dash-bootstrap-components==1.6.0
dash-leaflet==1.0.14
plotly==5.18.0
pandas==2.1.3
numpy==1.26.2
pymongo==4.6.0
python-dotenv==1.0.0
```

**4. Import dataset into MongoDB**
```bash
# From project root directory
mongoimport --type csv --headerline --db AAC --collection animals \
  --file aac_shelter_outcomes.csv
```

**5. Create database user with authentication**
```bash
# Start MongoDB shell
mongosh

# Switch to AAC database
use AAC

# Create user with read/write permissions
db.createUser({
  user: "aacuser",
  pwd: "your_secure_password",
  roles: [
    { role: "readWrite", db: "AAC" }
  ]
})

# Verify user creation
db.getUsers()
```

**6. Configure environment variables**

Create `.env` file in project root:
```env
MONGO_USER=aacuser
MONGO_PASSWORD=your_secure_password
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DATABASE=AAC
MONGO_COLLECTION=animals
```

**Security Note:** Never commit `.env` file to version control. It's included in `.gitignore`.

### Running the Application

**Method 1: Python Script (Recommended)**
```bash
# Ensure virtual environment is activated
python dashboard.py
```

Access dashboard at: `http://localhost:8050`

**Method 2: Jupyter Notebook (Development)**
```bash
# Convert dashboard.py to notebook if needed
jupyter notebook dashboard.ipynb
```

Run all cells to start the Dash server.

**Stopping the Application:**
- Terminal: Press `Ctrl+C`
- Jupyter: Interrupt kernel

## Usage Guide

### Filtering Animals by Rescue Type

1. Locate the **"Filter by Rescue Type"** dropdown near the top of the dashboard
2. Click the dropdown to reveal filter options:
   - Water Rescue
   - Mountain Rescue
   - Disaster Rescue
   - Reset
3. Select desired rescue type
4. Data table automatically updates to show only matching animals
5. Pie chart refreshes to show breed distribution of filtered results
6. First row auto-selects to display animal location on map

### Viewing Animal Details

1. **In Data Table:** Click any row to select an animal
2. **On Map:** 
   - Marker appears at animal's shelter location
   - **Hover** over marker to see breed in tooltip
   - **Click** marker to open popup with animal name
3. **In Pie Chart:** Hover over slice to see breed count and percentage

### Sorting Data

- Click any column header to sort ascending
- Click again to sort descending
- Click third time to remove sort

### Navigating Large Datasets

- Use pagination controls at bottom of table
- Table displays 10 records per page
- Current page indicator shows position in dataset
- Jump to specific page using page number buttons

### Resetting View

Select "Reset" from filter dropdown to return to unfiltered view of all 10,000+ shelter animals.

## Development Status

### ✅ Completed (Project One - Database Foundation)
- [x] MongoDB database setup and configuration
- [x] User authentication with role-based permissions
- [x] CRUD Python module with all four operations
- [x] Test script validating CRUD functionality
- [x] Error handling and input validation
- [x] Environment variable configuration for security

### ✅ Completed (Project Two - Dashboard Implementation)
- [x] Full dashboard layout with responsive design
- [x] Interactive data table with sorting and pagination
- [x] Dropdown filter with three rescue type queries + reset
- [x] MongoDB query integration for filtering
- [x] Pie chart visualization for breed distribution
- [x] Geolocation map with Leaflet integration
- [x] Real-time component updates via callbacks
- [x] Logo and branding integration
- [x] Custom styling with Bootstrap UNITED theme
- [x] Professional color palette and typography
- [x] Mobile-responsive grid layout
- [x] Row highlighting for selected table records
- [x] Additional chart types (bar chart for age distribution)
- [x] Export filtered results to CSV

### 🔄 In Progress
- [ ] Custom map markers with brand colors

### 📋 Planned Enhancements
- [ ] User authentication UI for dashboard access
- [ ] Role-based dashboard permissions
- [ ] Real-time data refresh from MongoDB change streams
- [ ] Advanced search with multi-field filtering
- [ ] Dashboard analytics and usage metrics
- [ ] Printable report generation
- [ ] Dark mode theme option
- [ ] Unit test suite with pytest
- [ ] Docker containerization for deployment
- [ ] CI/CD pipeline configuration

## Testing

### CRUD Module Tests

Located in `tests/test_crud.ipynb`:

```python
# Import module
from animal_shelter import AnimalShelter

# Initialize connection
shelter = AnimalShelter()

# Test Create
test_animal = {
    "animal_id": "TEST001",
    "animal_type": "Dog",
    "breed": "Golden Retriever",
    "name": "Test Dog",
    "age_upon_outcome_in_weeks": 52
}
result = shelter.create(test_animal)
print(f"Create success: {result}")  # Should print True

# Test Read
results = shelter.read({"animal_id": "TEST001"})
print(f"Found {len(results)} record(s)")

# Test Update
modified = shelter.update(
    {"animal_id": "TEST001"},
    {"name": "Updated Test Dog"}
)
print(f"Modified {modified} record(s)")

# Test Delete
deleted = shelter.delete({"animal_id": "TEST001"})
print(f"Deleted {deleted} record(s)")
```

### Dashboard Testing Checklist

**Filter Functionality:**
- [ ] Water Rescue filter returns correct breeds
- [ ] Mountain Rescue filter returns correct breeds
- [ ] Disaster Rescue filter returns correct breeds
- [ ] Reset filter shows all records
- [ ] First row auto-selects after filter change

**Data Table:**
- [ ] All columns display correctly
- [ ] Sorting works on each column
- [ ] Pagination navigates through records
- [ ] Row selection updates map

**Visualizations:**
- [ ] Pie chart displays top 8 breeds
- [ ] Chart updates when filter changes
- [ ] Hover tooltips show correct data
- [ ] Map centers on selected animal
- [ ] Map marker shows correct location
- [ ] Tooltip displays breed
- [ ] Popup shows animal name

**Responsive Design:**
- [ ] Layout adapts to mobile screens
- [ ] All elements remain accessible
- [ ] Text remains readable at all sizes

## Challenges and Solutions

### Challenge 1: Filter Reset Not Updating Selected Row
**Problem:** When applying new filter, first row wasn't auto-selecting, causing map to show stale data.

**Solution:** Modified `update_table` callback to return both filtered data AND `[0]` for selected_rows, ensuring first row is always selected after filter application.

```python
@app.callback(
    Output('shelter-table', 'data'),
    Output('shelter-table', 'selected_rows'),  # Added second output
    Input('dropdown-filter', 'value')
)
def update_table(dropdown_filter):
    # ... filter logic ...
    return filtered_df.to_dict('records'), [0]  # Always select first row
```

### Challenge 2: Pie Chart Overcrowding with Unfiltered Data
**Problem:** With 10,000+ records, pie chart displayed 100+ breeds, making it unreadable.

**Solution:** Implemented top-8 breed filtering using Pandas value_counts() to show only most common breeds in current dataset.

```python
top_breeds = pie_df['breed'].value_counts().head(8).reset_index()
```

### Challenge 3: Radio Button Styling
**Problem:** Default radio buttons didn't match brand colors and were difficult to see.

**Solution:** Applied inline CSS accent-color property via DataTable's css parameter to customize radio button color to brand red (#c9341b).

### Challenge 4: Snake Case Column Headers
**Problem:** Database field names like `age_upon_outcome_in_weeks` appeared as-is in table headers.

**Solution:** Transformed column names during DataTable initialization using Python string methods.

```python
columns=[{
    'name': i.replace('_', ' ').title(),  # Display name
    'id': i                                 # Original field name
} for i in df.columns]
```
### Challenge 5: Adding Chart Selection Without Breaking Layout
**Problem:** Wanted to add age distribution chart but didn't want two separate graph areas taking up space.

**Solution:** Implemented dropdown selector that toggles between chart types using the same graph container, with conditional rendering in the callback based on selector value.
```python
@app.callback(
    Output('chart-holder', 'figure'),
    [Input('shelter-table', 'derived_virtual_data'),
     Input('chart-selector', 'value')]
)
def update_pie_chart(viewData, chart_selector):
    if chart_selector == 'Breed Distribution':
        # ... return pie chart
    elif chart_selector == 'Age Distribution':
        # ... return bar chart
```

## Performance Considerations

- **Initial Load:** ~2-3 seconds for 10,000 records on standard broadband
- **Filter Application:** <500ms for query execution and table update
- **Map Rendering:** ~1 second for Leaflet initialization
- **Chart Updates:** Real-time (<100ms) due to client-side Pandas operations

**Optimization Opportunities:**
- Implement server-side pagination for datasets >50,000 records
- Cache frequent queries with TTL expiration
- Add database indexes on commonly filtered fields
- Lazy-load map tiles to reduce initial bandwidth

## Contributing

This project was developed as coursework for CS-340 (Client/Server Development) at Southern New Hampshire University. While this is academic work, the repository is public for portfolio purposes. Feedback, suggestions, and constructive criticism are welcome!

**If you'd like to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure code follows PEP 8 style guidelines and includes appropriate comments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Austin Animal Center** for providing the shelter outcomes dataset
- **Grazioso Salvare** (fictional client) for project requirements and specifications
- **MongoDB** documentation and community support
- **Plotly Dash** documentation and example galleries
- **Southern New Hampshire University** CS-340 course materials and instruction
- **Bootstrap** and **Dash Bootstrap Components** for UI framework

## Contact

**Sarah Dowd**
- Email: sarah.dowd1@snhu.edu
- GitHub: [@sldowd](https://github.com/sldowd)

---

*Last Updated: December 2025*  
*Project Version: 2.0.0 (Dashboard Complete)*