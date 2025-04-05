# Streamlit Dynamic Filter

This project is a Streamlit web app that allows users to apply dynamic filters to a dataset and view the results interactively. The dataset contains configurations for different system types and parts, which can be filtered based on various parameters.

## Features

- Select filters such as APPLICATION, BODY MFG, CHASSIS MANUFACTURE, and more.
- Dynamically display results based on the filter selections.
- View related system part numbers, kits needed, system cost, and installation costs.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/streamlit-dynamic-filter.git
    cd streamlit-dynamic-filter
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run dynamic_filter.py
    ```

## Usage

Once the app is running, use the dropdown menus to select filter categories such as APPLICATION, BODY MFG, CHASSIS TYPE, etc. The filtered data will be displayed based on your selections.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
