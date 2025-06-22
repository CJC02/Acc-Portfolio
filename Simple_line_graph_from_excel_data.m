% Read data from the Excel file into a table
data = readtable('Book1.xlsx');

% Extract 'x' and 'y' columns from the table
x = data.x;
y = data.y;

% Plot a simple line graph
plot(x, y, '-o')              % Line with circular markers
xlabel('x')                   % Label for x-axis
ylabel('y')                   % Label for y-axis
title('Line Graph from Excel Data')
grid on                      % Add a grid to the plot
