import re
class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        """
        The function is used to calculate the string numbers based on certain test params
        :param numbers: string that contains number
        :return: sum of the string
        """
        try:
            if not numbers:
                return 0

            # Default delimiters: comma and newline
            delimiters = [",", "\n"]
            custom_delimiter_pattern = r"^//(.+)\n"

            # Check for custom delimiter
            if numbers.startswith("//"):
                match = re.match(custom_delimiter_pattern, numbers)
                if match:
                    custom_delimiter = match.group(1)
                    delimiters.append(re.escape(custom_delimiter))
                    numbers = numbers[len(match.group(0)):]

            # Split numbers using all delimiters
            delimiter_pattern = "|".join(delimiters)
            num_list = re.split(delimiter_pattern, numbers)

            # Parse numbers and calculate the sum
            total = 0
            negatives = []
            for num in num_list:
                if num.strip():  # Ignore empty strings
                    value = int(num)
                    if value < 0:
                        negatives.append(value)
                    total += value

            # Handle negative numbers
            if negatives:
                print(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
            return total
        except Exception as e:
            print("Unexpected condition occurred " + str(e))
            return 0


# Example shared in the assessment
print(StringCalculator.add(""))
print(StringCalculator.add("1"))
print(StringCalculator.add("1,5"))
print(StringCalculator.add("1\n2,3"))
print(StringCalculator.add("//;\n1;2"))
print(StringCalculator.add("-1,2,-3"))
print(StringCalculator.add("-1,2,1.3"))
print(StringCalculator.add("-1,2,13"))
print(StringCalculator.add("2\n3,56"))
print(StringCalculator.add("//;\n3;23"))
