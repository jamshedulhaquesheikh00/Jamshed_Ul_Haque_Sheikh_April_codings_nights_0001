{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPaOzEgoiDXsU6WAnAC9OvB",
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
        "<a href=\"https://colab.research.google.com/github/jamshedulhaquesheikh00/Jamshed_Ul_Haque_Sheikh_April_codings_nights_0001/blob/main/03_if_statements.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 01_print_events.md"
      ],
      "metadata": {
        "id": "Ch_QRSY6e0rI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "TK1W3i3Ke2wo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def print_events(events):\n",
        "  \"\"\"\n",
        "  Prints each event in the given list.\n",
        "\n",
        "  Args:\n",
        "    events: A list of strings, where each string represents an event.\n",
        "  \"\"\"\n",
        "  if not events:\n",
        "    print(\"No events to print.\")\n",
        "    return\n",
        "\n",
        "  for event in events:\n",
        "    print(event)\n",
        "\n",
        "# Example usage:\n",
        "events1 = [\"Meeting with team\", \"Presentation at conference\", \"Birthday party\"]\n",
        "print_events(events1)\n",
        "\n",
        "events2 = []\n",
        "print_events(events2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_hsHJLjre9x0",
        "outputId": "71c4f39c-a0ac-4186-ddbf-5e544a43547a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Meeting with team\n",
            "Presentation at conference\n",
            "Birthday party\n",
            "No events to print.\n"
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
        "id": "lehPvx86gd_k"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)\n",
        "    for i in range(20):\n",
        "        print(i * 2)  # Use the 'i' value inside the for-loop\n",
        "\n",
        "# Call the main function when \"run\", no need to edit anything below!\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0ZBao53qgjsd",
        "outputId": "7aa83cd6-755d-4ae1-e9e1-a1687707555a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n",
            "22\n",
            "24\n",
            "26\n",
            "28\n",
            "30\n",
            "32\n",
            "34\n",
            "36\n",
            "38\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 02_international_voting_age.md"
      ],
      "metadata": {
        "id": "VVIer59qhlR6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "r6q1dEiQhnsC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    \"\"\"\n",
        "    This function will process and display information about international voting ages.\n",
        "    \"\"\"\n",
        "\n",
        "    # Dictionary to store countries and their voting ages\n",
        "    voting_ages = {\n",
        "        \"Argentina\": 16,\n",
        "        \"Brazil\": 16,\n",
        "        \"Austria\": 16,\n",
        "        \"Germany\": 18,\n",
        "        \"United States\": 18,\n",
        "        \"Canada\": 18,\n",
        "        \"India\": 18,\n",
        "        \"Pakistan\": 18,\n",
        "        \"United Kingdom\": 18,\n",
        "        \"South Africa\": 18,\n",
        "        \"Italy\": 18,\n",
        "        \"Japan\": 18,\n",
        "        \"France\": 18,\n",
        "        \"Australia\": 18,\n",
        "        \"New Zealand\": 18,\n",
        "        \"China\": 18,\n",
        "        \"Russia\": 18,\n",
        "        \"Indonesia\": 17,\n",
        "        \"Sweden\": 18,\n",
        "        \"Netherlands\": 18,\n",
        "        \"Denmark\": 18,\n",
        "        \"Norway\": 18,\n",
        "        \"Finland\": 18,\n",
        "        \"Spain\": 18,\n",
        "        \"Portugal\": 18,\n",
        "        \"Greece\": 17,\n",
        "        \"Turkey\": 18,\n",
        "        \"Mexico\": 18,\n",
        "        \"Egypt\": 18,\n",
        "        \"Nigeria\": 18,\n",
        "        \"Bangladesh\": 18,\n",
        "        \"Vietnam\": 18,\n",
        "        \"Philippines\": 18,\n",
        "        \"Thailand\": 18,\n",
        "        \"Malaysia\": 21,\n",
        "        \"Singapore\": 21,\n",
        "        \"Switzerland\": 18,\n",
        "        \"Ireland\": 18,\n",
        "        \"Israel\": 18,\n",
        "        \"Saudi Arabia\": 18,\n",
        "        \"United Arab Emirates\": 18,\n",
        "        \"Kuwait\": 21,\n",
        "        \"Qatar\": 18,\n",
        "        \"Oman\": 21,\n",
        "        \"Bahrain\": 20,\n",
        "        \"Jordan\": 18,\n",
        "        \"Morocco\": 18,\n",
        "        \"Algeria\": 18,\n",
        "        \"Tunisia\": 18,\n",
        "        \"Libya\": 18,\n",
        "        \"Sudan\": 18,\n",
        "        \"Kenya\": 18,\n",
        "        \"Ethiopia\": 18,\n",
        "        \"Tanzania\": 18,\n",
        "        \"Uganda\": 18,\n",
        "        \"Zimbabwe\": 18,\n",
        "        \"Zambia\": 18,\n",
        "        \"Botswana\": 18,\n",
        "        \"Namibia\": 18,\n",
        "        \"Angola\": 18,\n",
        "        \"Mozambique\": 18,\n",
        "        \"Madagascar\": 18,\n",
        "        \"Cameroon\": 20,\n",
        "        \"Ghana\": 18,\n",
        "        \"Ivory Coast\": 18,\n",
        "        \"Senegal\": 18,\n",
        "        \"Peru\": 18,\n",
        "        \"Colombia\": 18,\n",
        "        \"Venezuela\": 18,\n",
        "        \"Chile\": 18,\n",
        "        \"Ecuador\": 16,\n",
        "        \"Bolivia\": 18,\n",
        "        \"Paraguay\": 18,\n",
        "        \"Uruguay\": 18,\n",
        "        \"Cuba\": 16,\n",
        "        \"Dominican Republic\": 18,\n",
        "        \"Haiti\": 18,\n",
        "        \"Guatemala\": 18,\n",
        "        \"Honduras\": 18,\n",
        "        \"El Salvador\": 18,\n",
        "        \"Nicaragua\": 16,\n",
        "        \"Costa Rica\": 18,\n",
        "        \"Panama\": 18,\n",
        "    }\n",
        "\n",
        "    # Print the voting ages for each country\n",
        "    print(\"International Voting Ages:\")\n",
        "    for country, age in voting_ages.items():\n",
        "        print(f\"- {country}: {age} years\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J5ElJZAKhuBo",
        "outputId": "45fbac67-228a-4237-f576-4c864ba3f53a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "International Voting Ages:\n",
            "- Argentina: 16 years\n",
            "- Brazil: 16 years\n",
            "- Austria: 16 years\n",
            "- Germany: 18 years\n",
            "- United States: 18 years\n",
            "- Canada: 18 years\n",
            "- India: 18 years\n",
            "- Pakistan: 18 years\n",
            "- United Kingdom: 18 years\n",
            "- South Africa: 18 years\n",
            "- Italy: 18 years\n",
            "- Japan: 18 years\n",
            "- France: 18 years\n",
            "- Australia: 18 years\n",
            "- New Zealand: 18 years\n",
            "- China: 18 years\n",
            "- Russia: 18 years\n",
            "- Indonesia: 17 years\n",
            "- Sweden: 18 years\n",
            "- Netherlands: 18 years\n",
            "- Denmark: 18 years\n",
            "- Norway: 18 years\n",
            "- Finland: 18 years\n",
            "- Spain: 18 years\n",
            "- Portugal: 18 years\n",
            "- Greece: 17 years\n",
            "- Turkey: 18 years\n",
            "- Mexico: 18 years\n",
            "- Egypt: 18 years\n",
            "- Nigeria: 18 years\n",
            "- Bangladesh: 18 years\n",
            "- Vietnam: 18 years\n",
            "- Philippines: 18 years\n",
            "- Thailand: 18 years\n",
            "- Malaysia: 21 years\n",
            "- Singapore: 21 years\n",
            "- Switzerland: 18 years\n",
            "- Ireland: 18 years\n",
            "- Israel: 18 years\n",
            "- Saudi Arabia: 18 years\n",
            "- United Arab Emirates: 18 years\n",
            "- Kuwait: 21 years\n",
            "- Qatar: 18 years\n",
            "- Oman: 21 years\n",
            "- Bahrain: 20 years\n",
            "- Jordan: 18 years\n",
            "- Morocco: 18 years\n",
            "- Algeria: 18 years\n",
            "- Tunisia: 18 years\n",
            "- Libya: 18 years\n",
            "- Sudan: 18 years\n",
            "- Kenya: 18 years\n",
            "- Ethiopia: 18 years\n",
            "- Tanzania: 18 years\n",
            "- Uganda: 18 years\n",
            "- Zimbabwe: 18 years\n",
            "- Zambia: 18 years\n",
            "- Botswana: 18 years\n",
            "- Namibia: 18 years\n",
            "- Angola: 18 years\n",
            "- Mozambique: 18 years\n",
            "- Madagascar: 18 years\n",
            "- Cameroon: 20 years\n",
            "- Ghana: 18 years\n",
            "- Ivory Coast: 18 years\n",
            "- Senegal: 18 years\n",
            "- Peru: 18 years\n",
            "- Colombia: 18 years\n",
            "- Venezuela: 18 years\n",
            "- Chile: 18 years\n",
            "- Ecuador: 16 years\n",
            "- Bolivia: 18 years\n",
            "- Paraguay: 18 years\n",
            "- Uruguay: 18 years\n",
            "- Cuba: 16 years\n",
            "- Dominican Republic: 18 years\n",
            "- Haiti: 18 years\n",
            "- Guatemala: 18 years\n",
            "- Honduras: 18 years\n",
            "- El Salvador: 18 years\n",
            "- Nicaragua: 16 years\n",
            "- Costa Rica: 18 years\n",
            "- Panama: 18 years\n"
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
        "id": "QXlpwuWzigQm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "PETURKSBOUIPO_AGE : int = 16\n",
        "STANLAU_AGE : int = 25\n",
        "MAYENGUA_AGE : int = 48\n",
        "\n",
        "def main():\n",
        "    # Get the user's age\n",
        "    user_age = int(input(\"How old are you? \"))\n",
        "\n",
        "    # Check if the user can vote in Peturksbouipo\n",
        "    if user_age >= PETURKSBOUIPO_AGE:\n",
        "        print(\"You can vote in Peturksbouipo where the voting age is \" + str(PETURKSBOUIPO_AGE) + \".\")\n",
        "    else:\n",
        "        print(\"You cannot vote in Peturksbouipo where the voting age is \" + str(PETURKSBOUIPO_AGE) + \".\")\n",
        "\n",
        "    # Check if the user can vote in Stanlau\n",
        "    if user_age >= STANLAU_AGE:\n",
        "        print(\"You can vote in Stanlau where the voting age is \" + str(STANLAU_AGE) + \".\")\n",
        "    else:\n",
        "        print(\"You cannot vote in Stanlau where the voting age is \" + str(STANLAU_AGE) + \".\")\n",
        "\n",
        "    # Check if user can vote in Mayengua\n",
        "    if user_age >= MAYENGUA_AGE:\n",
        "        print(\"You can vote in Mayengua where the voting age is \" + str(MAYENGUA_AGE) + \".\")\n",
        "    else:\n",
        "        print(\"You cannot vote in Mayengua where the voting age is \" + str(MAYENGUA_AGE) + \".\")\n",
        "\n",
        "\n",
        "# There is no need to edit code beyond this point\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1HlaUf2Fijh8",
        "outputId": "8e6c1cc8-a43f-408c-9465-269f95460d2c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "How old are you? 16\n",
            "You can vote in Peturksbouipo where the voting age is 16.\n",
            "You cannot vote in Stanlau where the voting age is 25.\n",
            "You cannot vote in Mayengua where the voting age is 48.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 03_leap_year.md"
      ],
      "metadata": {
        "id": "PEoZdA-5jDSO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "Qw3WMI6-jJax"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def is_leap_year(year):\n",
        "  \"\"\"\n",
        "  Checks if a year is a leap year.\n",
        "\n",
        "  Args:\n",
        "    year: An integer representing the year.\n",
        "\n",
        "  Returns:\n",
        "    True if the year is a leap year, False otherwise.\n",
        "  \"\"\"\n",
        "  # Your code here\n",
        "  pass\n",
        "\n",
        "# Example usage:\n",
        "print(is_leap_year(2020))  # Should print True\n",
        "print(is_leap_year(2021))  # Should print False\n",
        "print(is_leap_year(1900))  # Should print False\n",
        "print(is_leap_year(2000))  # Should print True"
      ],
      "metadata": {
        "id": "EcjQPFp3jOXP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "85da64de-5e90-42fa-a309-1e458688d4dc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "None\n",
            "None\n",
            "None\n",
            "None\n"
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
        "id": "GgVpTTkkjo8Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def is_leap_year(year):\n",
        "  \"\"\"\n",
        "  Checks if a year is a leap year.\n",
        "\n",
        "  Args:\n",
        "    year: An integer representing the year.\n",
        "\n",
        "  Returns:\n",
        "    True if the year is a leap year, False otherwise.\n",
        "  \"\"\"\n",
        "  if year % 4 == 0:\n",
        "    if year % 100 == 0:\n",
        "      if year % 400 == 0:\n",
        "        return True\n",
        "      else:\n",
        "        return False\n",
        "    else:\n",
        "      return True\n",
        "  else:\n",
        "    return False\n",
        "\n",
        "# Example usage:\n",
        "print(is_leap_year(2020))  # Should print True\n",
        "print(is_leap_year(2021))  # Should print False\n",
        "print(is_leap_year(1900))  # Should print False\n",
        "print(is_leap_year(2000))  # Should print True"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gUgrwxE0juii",
        "outputId": "98c536a2-6d38-4241-a894-c913cdf39ca8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n",
            "False\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 4_tall_enough_to_ride.md"
      ],
      "metadata": {
        "id": "se6vNrenxo0N"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "rbYHc4kBxyvD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def print_events(events):\n",
        "  \"\"\"\n",
        "  Prints each event in the given list.\n",
        "\n",
        "  Args:\n",
        "    events: A list of strings, where each string represents an event.\n",
        "  \"\"\"\n",
        "  if not events:\n",
        "    print(\"No events to print.\")\n",
        "    return\n",
        "\n",
        "  for event in events:\n",
        "    print(event)\n",
        "\n",
        "# Example usage:\n",
        "events1 = [\"Meeting with team\", \"Presentation at conference\", \"Birthday party\"]\n",
        "print_events(events1)\n",
        "\n",
        "events2 = []\n",
        "print_events(events2)"
      ],
      "metadata": {
        "id": "kfNUUipHx4UO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8bfa7550-73d1-4e0f-a8b4-ef07120e67b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Meeting with team\n",
            "Presentation at conference\n",
            "Birthday party\n",
            "No events to print.\n"
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
        "id": "w3G17dGrx-1p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def can_ride_rollercoaster(height, min_height=48):\n",
        "  \"\"\"\n",
        "  Checks if a person is tall enough to ride a rollercoaster.\n",
        "\n",
        "  Args:\n",
        "    height: An integer representing the person's height in inches.\n",
        "    min_height: An optional integer representing the minimum height required to ride.\n",
        "                Defaults to 48 inches.\n",
        "\n",
        "  Returns:\n",
        "    True if the person is tall enough, False otherwise.\n",
        "  \"\"\"\n",
        "  return height >= min_height\n",
        "\n",
        "# Example usage:\n",
        "print(can_ride_rollercoaster(50))  # Should print True\n",
        "print(can_ride_rollercoaster(45))  # Should print False\n",
        "print(can_ride_rollercoaster(48))  # Should print True\n",
        "print(can_ride_rollercoaster(40, min_height=42)) # Should print False"
      ],
      "metadata": {
        "id": "e8tQAsbUyCOQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "29a9ddf7-6532-41cf-da0a-5b3be01f8dd7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n",
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 05_random_numbers.md"
      ],
      "metadata": {
        "id": "6Cdl5RPHyoA1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Starter Code"
      ],
      "metadata": {
        "id": "xzhh-BV6ysOH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def generate_random_numbers(count, start=1, end=100):\n",
        "  \"\"\"\n",
        "  Generates a list of random numbers within a specified range.\n",
        "\n",
        "  Args:\n",
        "    count: The number of random numbers to generate.\n",
        "    start: The starting value of the range (inclusive). Defaults to 1.\n",
        "    end: The ending value of the range (inclusive). Defaults to 100.\n",
        "\n",
        "  Returns:\n",
        "    A list of random integers.\n",
        "  \"\"\"\n",
        "  # Your code here\n",
        "  pass\n",
        "\n",
        "# Example usage:\n",
        "print(generate_random_numbers(5))  # Should print a list of 5 random numbers between 1 and 100\n",
        "print(generate_random_numbers(3, start=50, end=150)) # Should print a list of 3 random numbers between 50 and 150\n",
        "print(generate_random_numbers(1)) # should print a list of 1 random number between 1 and 100"
      ],
      "metadata": {
        "id": "ZtnQFXJZyw0s",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f1284404-5ef3-4eaf-ea3d-b44ad9608321"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "None\n",
            "None\n",
            "None\n"
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
        "id": "dtpM1gnpy2L1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def generate_random_numbers(count, start=1, end=100):\n",
        "  \"\"\"\n",
        "  Generates a list of random numbers within a specified range.\n",
        "\n",
        "  Args:\n",
        "    count: The number of random numbers to generate.\n",
        "    start: The starting value of the range (inclusive). Defaults to 1.\n",
        "    end: The ending value of the range (inclusive). Defaults to 100.\n",
        "\n",
        "  Returns:\n",
        "    A list of random integers.\n",
        "  \"\"\"\n",
        "  random_numbers = []\n",
        "  for _ in range(count):\n",
        "    random_numbers.append(random.randint(start, end))\n",
        "  return random_numbers\n",
        "\n",
        "# Example usage:\n",
        "print(generate_random_numbers(5))  # Should print a list of 5 random numbers between 1 and 100\n",
        "print(generate_random_numbers(3, start=50, end=150)) # Should print a list of 3 random numbers between 50 and 150\n",
        "print(generate_random_numbers(1)) # should print a list of 1 random number between 1 and 100"
      ],
      "metadata": {
        "id": "fg2T-9GMy5Qn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d812f09c-344d-4a03-bf47-112fd46f9c7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[11, 10, 2, 3, 50]\n",
            "[95, 124, 133]\n",
            "[75]\n"
          ]
        }
      ]
    }
  ]
}