<img width="100px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Tehran_Metro_Logo.svg/200px-Tehran_Metro_Logo.svg.png"/>

# Tehran Metro Graph Data

This repository contains data related to the Tehran Metro stations. The data is available in JSON format as a graph structure data, providing different options for utilizing the data.

## Repository Contents

1. `data/stations.json`: This file contains the Tehran Metro stations data in JSON format. It includes information such as station names, coordinates, and other relevant details.

## Data Structure (data/stations.json)

The data in this repository follows a specific structure to represent the Tehran Metro stations. Here's an overview of the structure:

### Station Properties

Each station is represented by an object containing the following properties:

- `"disabled"`: A boolean value indicating if the station is disabled or not.
- `"name"`: The name of the station in English.
- `"translations"`: An object containing translations of the station name in different languages.
  - `"fa"`: The name of the station in Persian (Farsi).
  - **_[Other Languages]_**: You can add more language translations as needed.
- `"colors"`: An array of color codes associated with the station. This can be used to represent the station on maps or in visualizations.
- `"lines"`: An array of line numbers associated with the station. This indicates the metro lines that pass through the station.

Example:

```json
{
    "Tajrish": {
        "name": "Tajrish",
        "translations":{
          "fa": "تجریش"
        },
        "lines": [1],
        "longitude": "51.433643000000004",
        "latitude": "35.804501",
        "address": "خیابان شریعتی-ضلع جنوب غربی میدان قدس",
        "wc": false,
        "coffeeShop": false,
        "groceryStore": false,
        "fastFood": false,
        "atm": false,
        "relations": ["Gheytariyeh"]
    },
    ...
}
```

### Station Relations

Each station can have relations with other stations. These relations are represented as an array of names within the station object.

Example:

```json
{
    "Gheytariyeh": {
        ...
        "relations": ["Tajrish", "Shahid Sadr"]
    },
    ...
}
```

## Contribution Guide

We welcome contributions to this project! To contribute, please follow these steps:

1. Open an issue describing the changes or additions you want to make.
2. Wait for the repository owner to review and accept your issue. If the issue requires significant implementation time, please ensure it is approved before starting.
3. Once approved, create a new branch from the `main` branch and commit your changes to this branch.
4. Submit a pull request (PR) from your branch to the `main` branch. If your changes require testing, create your PR to the `develop` branch instead.

**Important:** Please adhere to this workflow; otherwise, we may have to close PRs that do not follow these guidelines.

## License

The data in this repository is licensed under the [Open Data Commons License](https://opendatacommons.org/licenses/). Please refer to the license file for more details on the terms and conditions of using the data.

If you have any questions or suggestions regarding the data or this repository, feel free to open an issue or contact me.
