{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM29TEpWo0IpFp2slGztJZo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jamshedulhaquesheikh00/Jamshed_Ul_Haque_Sheikh_April_codings_nights_0001/blob/main/01_basics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 00_joke_bot.md"
      ],
      "metadata": {
        "id": "nwMIn_M_ZTsG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "B3vO25rpZ5bq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Joke Bot\n",
        "\n",
        "This is a very basic joke bot! It will tell you a random joke when you ask for one.\n",
        "\n",
        "## How to Use\n",
        "\n",
        "1.  **Run the script:** (Assuming there's a corresponding script in a language like Python) Execute the script that reads this file or has the joke logic.\n",
        "2.  **Ask for a joke:** The script will likely have a way for you to interact (e.g., typing a command).\n",
        "3.  **Enjoy the laughter!** (Hopefully!)\n",
        "\n",
        "## Jokes\n",
        "\n",
        "Here are a few jokes to get started:\n",
        "\n",
        "1.  Why don't scientists trust atoms?\n",
        "    > Because they make up everything!\n",
        "\n",
        "2.  What do you call a lazy kangaroo?\n",
        "    > Pouch potato!\n",
        "\n",
        "3.  Why did the bicycle fall over?\n",
        "    > Because it was two tired!\n",
        "\n",
        "## Further Development\n",
        "\n",
        "Here are some ideas for expanding this simple joke bot:\n",
        "\n",
        "* **More Jokes:** Add a larger and more diverse collection of jokes.\n",
        "* **Joke Categories:** Allow users to request jokes by category (e.g., knock-knock, puns).\n",
        "* **User Input:** Implement more sophisticated ways for users to interact with the bot.\n",
        "* **External Joke API:** Integrate with an external API to fetch jokes.\n",
        "* **Error Handling:** Add checks for invalid user input.\n",
        "\n",
        "---\n",
        "\n",
        "**Note:** This `.md` file likely serves as documentation or a data source for the jokes. The actual logic for the bot would be in a separate script (e.g., a `.py` file for Python)."
      ],
      "metadata": {
        "id": "ID8DshaGaDU9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# solution"
      ],
      "metadata": {
        "id": "f4WN6IBbc0g4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "import re\n",
        "\n",
        "def load_jokes(filepath=\"00_joke_bot.md\"):\n",
        "    \"\"\"Loads jokes from a Markdown file.\"\"\"\n",
        "    jokes = []\n",
        "    try:\n",
        "        with open(filepath, 'r') as f:\n",
        "            lines = f.readlines()\n",
        "\n",
        "        in_joke = False\n",
        "        question = \"\"\n",
        "        answer = \"\"\n",
        "        for line in lines:\n",
        "            line = line.strip()\n",
        "            if line.startswith(\"## Jokes\"):\n",
        "                in_joke = True\n",
        "                continue\n",
        "            elif in_joke and re.match(r\"^\\d+\\.\\s+(.*)\", line):\n",
        "                if question and answer:\n",
        "                    jokes.append((question, answer))\n",
        "                question = re.match(r\"^\\d+\\.\\s+(.*)\", line).group(1)\n",
        "                answer = \"\"\n",
        "            elif in_joke and line.startswith(\">\"):\n",
        "                answer = line[1:].strip()\n",
        "            elif in_joke and not line:  # Empty line after a joke\n",
        "                if question and answer:\n",
        "                    jokes.append((question, answer))\n",
        "                    question = \"\"\n",
        "                    answer = \"\"\n",
        "            elif in_joke and line.startswith(\"##\"): # Reached the next section\n",
        "                break\n",
        "\n",
        "        # Add the last joke if it exists\n",
        "        if question and answer:\n",
        "            jokes.append((question, answer))\n",
        "\n",
        "    except FileNotFoundError:\n",
        "        print(f\"Error: File not found at {filepath}\")\n",
        "    return jokes\n",
        "\n",
        "def tell_joke(jokes):\n",
        "    \"\"\"Randomly selects and prints a joke.\"\"\"\n",
        "    if not jokes:\n",
        "        print(\"No jokes available!\")\n",
        "        return\n",
        "\n",
        "    random_joke = random.choice(jokes)\n",
        "    print(random_joke[0])\n",
        "    input(\"...\")  # Pause for effect\n",
        "    print(random_joke[1])\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    jokes = load_jokes()\n",
        "    tell_joke(jokes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TfvGXF8Vc3UJ",
        "outputId": "b3cb8008-5e3e-43d9-b65b-fc9b31ea93c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error: File not found at 00_joke_bot.md\n",
            "No jokes available!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 01_double_it.md"
      ],
      "metadata": {
        "id": "zi5_zDOhdvq8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "dJOTSdVXd9Wy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "import re\n",
        "\n",
        "def load_jokes(filepath=\"00_joke_bot.md\"):\n",
        "    \"\"\"Loads jokes from a Markdown file.\"\"\"\n",
        "    jokes = []\n",
        "    try:\n",
        "        with open(filepath, 'r') as f:\n",
        "            lines = f.readlines()\n",
        "\n",
        "        in_joke = False\n",
        "        question = \"\"\n",
        "        answer = \"\"\n",
        "        for line in lines:\n",
        "            line = line.strip()\n",
        "            if line.startswith(\"## Jokes\"):\n",
        "                in_joke = True\n",
        "                continue\n",
        "            elif in_joke and re.match(r\"^\\d+\\.\\s+(.*)\", line):\n",
        "                if question and answer:\n",
        "                    jokes.append((question, answer))\n",
        "                question = re.match(r\"^\\d+\\.\\s+(.*)\", line).group(1)\n",
        "                answer = \"\"\n",
        "            elif in_joke and line.startswith(\">\"):\n",
        "                answer = line[1:].strip()\n",
        "            elif in_joke and not line:  # Empty line after a joke\n",
        "                if question and answer:\n",
        "                    jokes.append((question, answer))\n",
        "                    question = \"\"\n",
        "                    answer = \"\"\n",
        "            elif in_joke and line.startswith(\"##\"): # Reached the next section\n",
        "                break\n",
        "\n",
        "        # Add the last joke if it exists\n",
        "        if question and answer:\n",
        "            jokes.append((question, answer))\n",
        "\n",
        "    except FileNotFoundError:\n",
        "        print(f\"Error: File not found at {filepath}\")\n",
        "    return jokes\n",
        "\n",
        "def tell_joke(jokes):\n",
        "    \"\"\"Randomly selects and prints a joke.\"\"\"\n",
        "    if not jokes:\n",
        "        print(\"No jokes available!\")\n",
        "        return\n",
        "\n",
        "    random_joke = random.choice(jokes)\n",
        "    print(random_joke[0])\n",
        "    input(\"...\")  # Pause for effect\n",
        "    print(random_joke[1])\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    jokes = load_jokes()\n",
        "    tell_joke(jokes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IvNkufdIeD_2",
        "outputId": "e217aa8a-9bb2-4543-d41a-781a2b696aed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error: File not found at 00_joke_bot.md\n",
            "No jokes available!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Solution"
      ],
      "metadata": {
        "id": "Pnhx9iLqek8s"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Python"
      ],
      "metadata": {
        "id": "T1aCGAvmf9ZH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def double_number(num):\n",
        "    return num * 2\n",
        "\n",
        "input_number = 12\n",
        "doubled_number = double_number(input_number)\n",
        "print(f\"The double of {input_number} is: {doubled_number}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FZaAPIHjgAML",
        "outputId": "fc4d88c8-f87e-4d93-9880-fd7de6c6a01d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The double of 12 is: 24\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 02_liftoff.md"
      ],
      "metadata": {
        "id": "LC9QcZmtiFC-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "D30TXnlNiNE4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class DoubleNumber {\n",
        "  constructor(num) {\n",
        "    this.num = num;\n",
        "  }\n",
        "\n",
        "  double() {\n",
        "    return this.num * 2;\n",
        "  }\n",
        "}\n",
        "\n",
        "const inputNumber = 12;\n",
        "const doubledNumber = new DoubleNumber(inputNumber).double();\n",
        "console.log(`The double of ${inputNumber} is: ${doubledNumber}`);"
      ],
      "metadata": {
        "id": "utjuzlVnjV3U"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Solution"
      ],
      "metadata": {
        "id": "MNww4la9fE2K"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class DoubleNumber:\n",
        "    def __init__(self, num):\n",
        "        self.num = num\n",
        "\n",
        "    def double(self):\n",
        "        return self.num * 2\n",
        "\n",
        "input_number = 12\n",
        "doubled_number = DoubleNumber(input_number).double()\n",
        "print(f\"The double of {input_number} is: {doubled_number}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6REyY_QQfLxQ",
        "outputId": "b414e6e2-7f34-4b21-f9b0-291469a8a8a2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The double of 12 is: 24\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 03_guess_my_number.md"
      ],
      "metadata": {
        "id": "5HLcpWKCoPhW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "vwMXBsBDqBeU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def guess_my_number():\n",
        "    secret_number = random.randint(1, 100)\n",
        "    attempts = 0\n",
        "\n",
        "    print(\"Welcome to the Guess My Number game!\")\n",
        "    print(\"I'm thinking of a number between 1 and 100.\")\n",
        "\n",
        "    while True:\n",
        "        try:\n",
        "            guess_str = input(\"Take a guess: \")\n",
        "            guess = int(guess_str)\n",
        "            attempts += 1\n",
        "\n",
        "            if guess < secret_number:\n",
        "                print(\"Too low! Try again.\")\n",
        "            elif guess > secret_number:\n",
        "                print(\"Too high! Try again.\")\n",
        "            else:\n",
        "                print(f\"Congratulations! You guessed the number {secret_number} in {attempts} attempts.\")\n",
        "                break\n",
        "        except ValueError:\n",
        "            print(\"Invalid input. Please enter a whole number.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    guess_my_number()"
      ],
      "metadata": {
        "id": "1UcHmZEXqIEF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Solution"
      ],
      "metadata": {
        "id": "1OHN6wSTrbcF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def guess_my_number():\n",
        "    secret_number = random.randint(1, 100)\n",
        "    attempts = 0\n",
        "\n",
        "    print(\"Welcome to the Guess My Number game!\")\n",
        "    print(\"I'm thinking of a number between 1 and 100.\")\n",
        "\n",
        "    while True:\n",
        "        try:\n",
        "            guess_str = input(\"Take a guess: \")\n",
        "            guess = int(guess_str)\n",
        "            attempts += 1\n",
        "\n",
        "            if guess < secret_number:\n",
        "                print(\"Too low! Try again.\")\n",
        "            elif guess > secret_number:\n",
        "                print(\"Too high! Try again.\")\n",
        "            else:\n",
        "                print(f\"Congratulations! You guessed the number {secret_number} in {attempts} attempts.\")\n",
        "                break\n",
        "        except ValueError:\n",
        "            print(\"Invalid input. Please enter a whole number.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    guess_my_number()"
      ],
      "metadata": {
        "id": "H2rrPAzYrhmx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 04_random_numbers.md"
      ],
      "metadata": {
        "id": "CW30zg1tsae6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "nHVIzrpHtF_e"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "print(\"Generating a random float between 0.0 and 1.0:\")\n",
        "random_float = random.random()\n",
        "print(random_float)\n",
        "\n",
        "print(\"\\nGenerating a random integer within a specific range (inclusive):\")\n",
        "random_integer = random.randint(1, 10)\n",
        "print(random_integer)\n",
        "\n",
        "print(\"\\nGenerating a random integer within a specific range (exclusive of the upper bound):\")\n",
        "random_range = random.randrange(1, 10)\n",
        "print(random_range)\n",
        "\n",
        "print(\"\\nChoosing a random element from a list:\")\n",
        "my_list = [\"apple\", \"banana\", \"cherry\"]\n",
        "random_element = random.choice(my_list)\n",
        "print(random_element)\n",
        "\n",
        "print(\"\\nChoosing multiple random elements from a list (with replacement):\")\n",
        "random_elements_with_replacement = random.choices(my_list, k=2)\n",
        "print(random_elements_with_replacement)\n",
        "\n",
        "print(\"\\nChoosing multiple unique random elements from a list (without replacement):\")\n",
        "random_elements_without_replacement = random.sample(my_list, k=2)\n",
        "print(random_elements_without_replacement)\n",
        "\n",
        "print(\"\\nShuffling the elements of a list in place:\")\n",
        "my_other_list = [1, 2, 3, 4, 5]\n",
        "print(\"Original list:\", my_other_list)\n",
        "random.shuffle(my_other_list)\n",
        "print(\"Shuffled list:\", my_other_list)\n",
        "\n",
        "print(\"\\nGenerating a random float within a specific range:\")\n",
        "start = 10.0\n",
        "end = 20.0\n",
        "random_in_range = random.uniform(start, end)\n",
        "print(random_in_range)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wp6PeaXstMzz",
        "outputId": "12535a55-d546-4350-a99e-5034d2846652"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Generating a random float between 0.0 and 1.0:\n",
            "0.31990885502119626\n",
            "\n",
            "Generating a random integer within a specific range (inclusive):\n",
            "8\n",
            "\n",
            "Generating a random integer within a specific range (exclusive of the upper bound):\n",
            "8\n",
            "\n",
            "Choosing a random element from a list:\n",
            "cherry\n",
            "\n",
            "Choosing multiple random elements from a list (with replacement):\n",
            "['cherry', 'apple']\n",
            "\n",
            "Choosing multiple unique random elements from a list (without replacement):\n",
            "['banana', 'cherry']\n",
            "\n",
            "Shuffling the elements of a list in place:\n",
            "Original list: [1, 2, 3, 4, 5]\n",
            "Shuffled list: [1, 4, 5, 2, 3]\n",
            "\n",
            "Generating a random float within a specific range:\n",
            "17.632054991114607\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Solution"
      ],
      "metadata": {
        "id": "cloxomCOuDPT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "# Generating a random float between 0.0 and 1.0\n",
        "random_float = random.random()\n",
        "print(f\"Random float (0.0 to 1.0): {random_float}\")\n",
        "\n",
        "# Generating a random integer within a specific range (inclusive)\n",
        "random_integer = random.randint(1, 10)\n",
        "print(f\"Random integer (1 to 10 inclusive): {random_integer}\")\n",
        "\n",
        "# Generating a random integer within a specific range (exclusive of the upper bound)\n",
        "random_range = random.randrange(1, 10)\n",
        "print(f\"Random range (1 to 9 inclusive): {random_range}\")\n",
        "\n",
        "# Choosing a random element from a list\n",
        "my_list = [\"apple\", \"banana\", \"cherry\"]\n",
        "random_element = random.choice(my_list)\n",
        "print(f\"Random element from list: {random_element}\")\n",
        "\n",
        "# Choosing multiple random elements from a list (with replacement)\n",
        "random_elements_with_replacement = random.choices(my_list, k=2)\n",
        "print(f\"Random elements with replacement: {random_elements_with_replacement}\")\n",
        "\n",
        "# Choosing multiple unique random elements from a list (without replacement)\n",
        "random_elements_without_replacement = random.sample(my_list, k=2)\n",
        "print(f\"Random elements without replacement: {random_elements_without_replacement}\")\n",
        "\n",
        "# Shuffling the elements of a list in place\n",
        "my_other_list = [1, 2, 3, 4, 5]\n",
        "print(f\"Original list: {my_other_list}\")\n",
        "random.shuffle(my_other_list)\n",
        "print(f\"Shuffled list: {my_other_list}\")\n",
        "\n",
        "# Generating a random float within a specific range\n",
        "start = 10.0\n",
        "end = 20.0\n",
        "random_in_range = random.uniform(start, end)\n",
        "print(f\"Random float in range ({start} to {end}): {random_in_range}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LNfhUenNuIDA",
        "outputId": "8a244466-6afd-4639-f24a-6e4c954645ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Random float (0.0 to 1.0): 0.12188369914320751\n",
            "Random integer (1 to 10 inclusive): 8\n",
            "Random range (1 to 9 inclusive): 7\n",
            "Random element from list: cherry\n",
            "Random elements with replacement: ['apple', 'banana']\n",
            "Random elements without replacement: ['banana', 'cherry']\n",
            "Original list: [1, 2, 3, 4, 5]\n",
            "Shuffled list: [5, 3, 1, 2, 4]\n",
            "Random float in range (10.0 to 20.0): 10.1261773140539\n"
          ]
        }
      ]
    }
  ]
}