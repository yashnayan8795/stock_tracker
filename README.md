#stock_tracker
                  Stock Price Tracker

This is a web-based application that allows users to track real-time stock prices. Built with Flask, jQuery, and yFinance, the app fetches and displays the latest stock prices for user-specified tickers. Users can add or remove tickers and see updates every 15 seconds, with color-coded indicators showing price changes.

Features:
  -Real-time Stock Data: Fetches and displays the latest stock prices using yFinance.
  -User Management: Add or remove stock tickers to track.
  -Auto-Refresh: Updates stock prices every 15 seconds.
  -Visual Indicators: Color-coded price changes for quick insights.
  -Persistent Storage: Uses local storage to remember user-selected tickers


#Technologies:

    Frontend: HTML, CSS, jQuery
    Backend: Flask (Python)
    Data Source: yFinance API


#Installation:

  1.Clone the repository:
  
    git clone https://github.com/yourusername/stock-price-tracker.git
    cd stock-price-tracker
  
  2.Create and activate a virtual environment:
    
    python -m venv venv
    venv\Scripts\activate  # On Mac OS use `source venv/bin/activate`
  
  3.Install the required dependencies(optional):
    pip install -r requirements.txt

#Usage:

  1.Start the Flask server:
      python main.py
  
  2.Open your browser and go to:
  
    http://127.0.0.1:5000 (or on your local host server displayed in your terminal)
    
  3.Add stock tickers:
  
    Enter a stock ticker in the input field and click "Add".
    The stock price and percentage change will be displayed and updated every 15 seconds.

#File Structure:
    main.py: The main Flask application file.
    templates/
        index.html: The main HTML file.
    static/
        style.css: CSS styles for the application.
        script.js: JavaScript for handling dynamic content and interactions.
        requirements.txt: A list of Python dependencies.

#Contributing:

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


#Screenshot:

<img width="926" alt="image" src="https://github.com/yashnayan8795/stock_tracker/assets/115628084/a5506ced-196c-4cbe-bab0-9b585218d6d5">


#License:
This project is licensed under the MIT License. See the LICENSE file for details.


Feel free to replace the placeholder URL for cloning the repository and add a screenshot image in your project directory to use in the README.
