# Random Number Generator

This project is a Python application that generates random numbers from various statistical distributions and visualizes the results using histograms. The user can specify the sample size and distribution parameters, and the application will generate the corresponding random numbers.

## Features

- Generate random numbers from:
  - Uniform distribution
  - Exponential distribution
  - Normal distribution
- Visualize the generated numbers using frequency histograms.
- User-friendly input handling for sample size and distribution parameters.

## Installation

To run this application, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. Clone the repository:
   ```
   git clone <repository-url>
   cd random-number-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to input:
   - Desired sample size (up to 1,000,000)
   - Distribution type (uniform, exponential, normal)
   - Required parameters based on the selected distribution
   - Number of intervals for the histogram (10, 15, 20, or 25)

3. The application will generate the random numbers and display a histogram of the observed frequencies.

## Example

- For a uniform distribution, you might input:
  - Sample size: 1000
  - Distribution parameters: a = 0, b = 10
  - Number of intervals: 15

- For an exponential distribution, you might input:
  - Sample size: 500
  - Rate parameter: λ = 1
  - Number of intervals: 20

- For a normal distribution, you might input:
  - Sample size: 1000
  - Mean: 0, Standard deviation: 1
  - Number of intervals: 25

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.