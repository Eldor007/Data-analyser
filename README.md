
# 3D Comparison Plotter for Room Type, Price, and Distance to City Center

## Overview

This Python script generates 3D plots to compare room types, prices, and the distance to the city center for both weekdays and weekends. It is designed to visually represent how these factors vary across different room types, providing insight into pricing trends and proximity to city centers.

The tool filters the data to only include rooms with a price of 2000 or less, making the analysis more focused on affordable options.

## Features

- **3D Plots**: The script generates two distinct 3D plots for weekdays and weekends, each showing the relationship between room type, price, and distance to the city center.
- **Custom Color Palette**: Different room types are represented with unique colors using `seaborn`'s color palette to ensure visual clarity.
- **Interactive Visualization**: The 3D plots are interactive, allowing users to explore the data from different angles.
  
## Prerequisites

- Python 3.7+
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

To install the required packages, use:

```bash
pip install pandas matplotlib seaborn
```

## Usage

1. Prepare your data for both weekdays and weekends as pandas DataFrames. The data should contain at least the following columns:
   - `room_type`: The type of the room (e.g., "Entire home/apt", "Private room").
   - `realSum`: The price of the room.
   - `distance`: The distance of the room to the city center.

2. Load the data into the script and call the `create_comparison_3d_plots(weekdays_data, weekends_data)` function.

3. The function will generate two 3D plots for weekdays and weekends that can be viewed interactively.

### Example

Here is an example of how to use the script:

```python
import pandas as pd
from job import create_comparison_3d_plots

# Example data for weekdays and weekends
weekdays_data = pd.read_csv('weekdays_data.csv')
weekends_data = pd.read_csv('weekends_data.csv')

# Create the 3D comparison plots
create_comparison_3d_plots(weekdays_data, weekends_data)
```

## Customization

- **Room Types**: The color palette automatically adapts to the number of unique room types in your data.
- **Price Filter**: By default, the script filters out prices above 2000. You can modify this limit by adjusting the filter in the code:
  
```python
weekdays_data = weekdays_data[weekdays_data['realSum'] <= 2000]
weekends_data = weekends_data[weekends_data['realSum'] <= 2000]
```

## License

This project is open-source and free to use under the MIT License.
