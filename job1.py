
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Function to create 3D plots for room type, price, and distance to city center comparison
def create_comparison_3d_plots(weekdays_data, weekends_data):
    # Filter the data to include only prices <= 2000
    weekdays_data = weekdays_data[weekdays_data['realSum'] <= 2000]
    weekends_data = weekends_data[weekends_data['realSum'] <= 2000]

    # Set a custom color palette for different room types
    room_types = weekdays_data['room_type'].unique()
    colors = sns.color_palette("husl", len(room_types))  # Use a distinct color for each room type
    color_map = {room_type: colors[i] for i, room_type in enumerate(room_types)}

    # Create a figure with two 3D subplots for Room Type, Price, and Distance to City Center
    fig1 = plt.figure(figsize=(12, 5.3))  # Reduced size by 1.5 times

    # First 3D Plot: Weekdays
    ax1 = fig1.add_subplot(121, projection='3d')
    for room_type in room_types:
        filtered_data = weekdays_data[weekdays_data['room_type'] == room_type]
        ax1.scatter(filtered_data['distance'], filtered_data['realSum'], filtered_data['room_type'], 
                    color=color_map[room_type], label=room_type)
    ax1.set_title('Weekdays')
    ax1.set_xlabel('Distance to City Center')
    ax1.set_ylabel('Price')
    ax1.set_zlabel('Room Type')
    ax1.legend()

    # Second 3D Plot: Weekends
    ax2 = fig1.add_subplot(122, projection='3d')
    for room_type in room_types:
        filtered_data = weekends_data[weekends_data['room_type'] == room_type]
        ax2.scatter(filtered_data['distance'], filtered_data['realSum'], filtered_data['room_type'], 
                    color=color_map[room_type], label=room_type)
    ax2.set_title('Weekends')
    ax2.set_xlabel('Distance to City Center')
    ax2.set_ylabel('Price')
    ax2.set_zlabel('Room Type')
    ax2.legend()

    plt.show()

# Example usage (replace 'weekdays_data.csv' and 'weekends_data.csv' with your actual data file paths)
if __name__ == "__main__":
    weekdays_data = pd.read_csv('weekdays_data.csv')  # Replace with actual data file
    weekends_data = pd.read_csv('weekends_data.csv')  # Replace with actual data file
    
    create_comparison_3d_plots(weekdays_data, weekends_data)
