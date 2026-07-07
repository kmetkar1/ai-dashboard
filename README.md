# 🤖 AI Implementation Dashboard

An interactive, enterprise-grade dashboard for tracking AI project implementations across your organization.

## 📊 Features

- **Real-time Data Visualization**: Interactive charts showing AI implementation across categories
- **Advanced Filtering**: Filter by Region, Market, and Industry
- **AI Category Tracking**:
  - Agentic AI
  - AI Ops
  - Business Transformation
  - ICA (Intelligent Content Automation)
- **Detailed Project View**: Comprehensive table with all project details
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Auto-refresh**: Dashboard updates automatically when you modify the data

## 🚀 Quick Start

### Option 1: Using the Batch File (Easiest - Windows)
1. Double-click `START_DASHBOARD.bat`
2. The dashboard will open automatically in your browser
3. Press Ctrl+C in the terminal to stop the server

### Option 2: Using Python
1. Open terminal/command prompt
2. Navigate to the AI_Projects_Dashboard folder
3. Run: `python -m http.server 8000`
4. Open browser and go to: `http://localhost:8000/dashboard.html`

### Option 3: Using Node.js
1. Install http-server: `npm install -g http-server`
2. Navigate to the AI_Projects_Dashboard folder
3. Run: `http-server -p 8000`
4. Open browser and go to: `http://localhost:8000/dashboard.html`

## 📝 Updating Data

### Method 1: Edit CSV File Directly
1. Open `data/projects_data.csv` in Excel or any text editor
2. Modify the data as needed
3. Save the file
4. Refresh the dashboard in your browser (F5)

### Method 2: Replace with Your Own Data
1. Export your project data to CSV format
2. Ensure it has these columns:
   - Project_ID
   - Project_Name
   - Region
   - Market
   - Industry
   - AI_Category
   - Agentic_AI (Yes/No)
   - AI_Ops (Yes/No)
   - Business_Transformation (Yes/No)
   - ICA (Yes/No)
   - Budget
   - Status
   - Start_Date
3. Replace `data/projects_data.csv` with your file
4. Refresh the dashboard

## 📋 Data Format

### CSV Structure
```csv
Project_ID,Project_Name,Region,Market,Industry,AI_Category,Agentic_AI,AI_Ops,Business_Transformation,ICA,Budget,Status,Start_Date
P001,Customer Service Automation,North America,Enterprise,Banking,Agentic AI,Yes,No,Yes,No,500000,Active,2024-01-15
```

### Field Descriptions
- **Project_ID**: Unique identifier for the project
- **Project_Name**: Name of the project
- **Region**: Geographic region (North America, Europe, Asia Pacific, Latin America, etc.)
- **Market**: Market segment (Enterprise, Mid-Market, SMB)
- **Industry**: Industry vertical (Banking, Healthcare, Retail, etc.)
- **AI_Category**: Primary AI category (Agentic AI, AI Ops, Business Transformation, ICA)
- **Agentic_AI**: Whether project uses Agentic AI (Yes/No)
- **AI_Ops**: Whether project uses AI Ops (Yes/No)
- **Business_Transformation**: Whether project involves business transformation (Yes/No)
- **ICA**: Whether project uses Intelligent Content Automation (Yes/No)
- **Budget**: Project budget in dollars (numeric)
- **Status**: Project status (Active, Completed, etc.)
- **Start_Date**: Project start date (YYYY-MM-DD)

## 🎨 Dashboard Components

### Header Section
- Total Projects count
- Active Projects count
- Total Budget (in millions)

### Filters
- **Region Filter**: Filter projects by geographic region
- **Market Filter**: Filter by market segment
- **Industry Filter**: Filter by industry vertical
- **Reset Button**: Clear all filters

### Metrics Cards
- Agentic AI project count
- AI Ops project count
- Business Transformation project count
- ICA project count

### Visualizations
1. **AI Category Distribution** (Doughnut Chart)
2. **Industry-wise AI Implementation** (Bar Chart)
3. **Regional Distribution** (Pie Chart)
4. **Market Segment Analysis** (Bar Chart)

### Project Details Table
Comprehensive table showing all project information with color-coded badges

## 🛠️ Customization

### Changing Colors
Edit the CSS in `dashboard.html` to customize colors:
- Gradient backgrounds
- Chart colors
- Badge colors
- Card colors

### Adding New Filters
1. Add new filter dropdown in the HTML
2. Update the `applyFilters()` function in JavaScript
3. Add filter logic to match your data

### Adding New Charts
1. Add a new canvas element in HTML
2. Create chart using Chart.js in the `updateCharts()` function
3. Process your data and pass to the chart

## 📱 Browser Compatibility

- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Edge
- ✅ Safari
- ✅ Opera

## 🔧 Troubleshooting

### Dashboard shows "Loading data..."
- Ensure you're running a local server (not opening HTML directly)
- Check that `data/projects_data.csv` exists
- Verify CSV file is properly formatted

### Charts not displaying
- Check browser console for errors (F12)
- Ensure internet connection (for Chart.js CDN)
- Verify data format in CSV

### Filters not working
- Refresh the page
- Check that filter values match data in CSV
- Clear browser cache

## 📦 File Structure

```
AI_Projects_Dashboard/
├── dashboard.html          # Main dashboard file
├── START_DASHBOARD.bat     # Windows batch file to start server
├── start_dashboard.py      # Python script to start server
├── README.md              # This file
└── data/
    └── projects_data.csv  # Project data (EDIT THIS FILE)
```

## 💡 Tips for Management Presentation

1. **Before the Meeting**:
   - Update CSV with real project data
   - Test all filters
   - Take screenshots of key metrics

2. **During Presentation**:
   - Start with overview metrics (header stats)
   - Show category distribution
   - Demonstrate filters with real scenarios
   - Drill down into specific projects using the table

3. **Interactive Demo**:
   - Filter by region to show geographic distribution
   - Filter by industry to show sector focus
   - Combine filters to answer specific questions

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify data format matches the specification
3. Ensure you're running a local server

## 🎯 Next Steps

1. Replace dummy data with your actual project data
2. Customize colors to match your company branding
3. Add additional metrics if needed
4. Export charts as images for presentations
5. Schedule regular data updates

---

**Version**: 1.0  
**Last Updated**: 2024  
**License**: MIT