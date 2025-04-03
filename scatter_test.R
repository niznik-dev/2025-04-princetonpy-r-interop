# Load the ggplot2 library
library(ggplot2)

# Create example data
data <- data.frame(
  x = rnorm(100, mean = 50, sd = 10),  # Random x values
  y = rnorm(100, mean = 30, sd = 5)    # Random y values
)

# Generate a scatter plot
plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point(color = "blue", size = 2) +  # Scatter points
  labs(title = "Scatter Plot Example", x = "X-Axis", y = "Y-Axis") +
  theme_minimal()

# Save the plot to a file
ggsave("scatter_plot.png", plot, width = 6, height = 4)

# Save the data to a CSV file
write.csv(data, "scatter_data.csv", row.names = FALSE)

data