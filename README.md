
![DALLE2025-01-0700 54 00-Afuturisticandmodernillustrationshowcasingarandomcharactergeneratorconcept Aglowinghumanoidfigureinthecentersurroundedbyfloatingd-ezgif com-webp-to-jpg-converter](https://github.com/user-attachments/assets/1445a426-36aa-44c0-91a4-134a86907c6a)

# Fake-Identity-Generator
This Python program generates a random fictional character with full identity details, including personal information, contact details, financial information, physical appearance, personality traits, and fantasy features.
# Random Character Generator

## Features
- **Basic Identity Information**:
  - Gender, First Name, Middle Name, Last Name, Initials, Mother's Maiden Name
- **Date of Birth and Zodiac Sign**
- **Login Details**:
  - Username, Password, Password Hashes (MD5, SHA1)
- **Contact Information**:
  - Email, Phone, Address
- **Financial Information**:
  - Credit Card Number, Social Security Number (SSN), Passport Details, Driver's License Details
- **Physical Appearance**:
  - Hair Color, Eye Color, Height, Weight, Blood Type
- **Personality Traits**:
  - Religion, Political Affiliation, Favorite Color, Comfort Food, Favorite Season
- **Fantasy Features**:
  - D&D-style Alignment and Ability Scores

## Requirements
- Python 3.6 or higher
- Install the following Python library:
  ```
  pip install faker
  ```

## Usage
1. Clone or download the repository.
2. Run the `random_character_generator.py` script:
   ```
   python random_character_generator.py
   ```
3. The program will output a randomly generated character profile in the console.

## How It Works
- The program uses the `Faker` library to generate realistic names, addresses, and other data.
- Randomization ensures each character is unique.
- Password hashes are generated using Python's `hashlib` module.

## Example Output
```
Gender	Female
First name	Jessie
Middle name	Janie
Last name	Mann
Initials	J. J. M.
Mother's Maiden name	Gardner
Birthday	June, 05 1994 (Age: 30 years)
Zodiacal sign	Gemini
User name	j.m.159
Password	1vlspk4lt
Password hash (MD5)	e788c0118a8b6fd34592bec9c42863f3
Password hash (SHA1)	0d6655393797a733293e1a44016aeb801c0181ec
E-Mail	j.m.159@suremail.info
Phone	376-469-8358
Address	13 W 7th St, Los Angeles, CA 90057, USA
Credit Card	4498746305739756
SSN	391112766 - issued in Wisconsin (WI)
Passport	No.: 670538688
issued: January/07/2020
expires: January/06/2030
Driver License	D3070041 - issued in California (CA) on 08/01/2023, expires 06/05/2027
Hair color	Brown (BRO)
Eyes color	Green (GRN)
Height	170 cm / 5 ft 7 in
Weight	65 Kg / 143 pounds
Blood Type	O+
Religion	Unaffiliated Believer
Political side	Republican
Favorite Color	Pink
Favorite Comfort Food	Macaroni and Cheese
Favorite Season	Winter
Alignment	Neutral Evil
Abilities 	Charisma: 10
Constitution: 16
Dexterity: 17
Intelligence: 9
Strength: 3
Wisdom: 5
```

## Customization
You can customize the ranges and options for generated data in the script, such as:
- Gender options
- Birthdate ranges
- Password complexity
- Fantasy alignment and abilities

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions and suggestions are welcome! Feel free to fork the repository and submit a pull request.

## Author
Created by [Your Name].

