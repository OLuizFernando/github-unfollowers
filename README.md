# GitHub Unfollowers

A Python script that identifies GitHub users you follow but who do not follow you back. It uses the GitHub API to fetch and compare the "followers" and "following" lists for a given username.

## Features

- Fetches all followers and following using GitHub API with authentication.
- Identifies users you follow who do not follow you back.
- Outputs a list of unfollowers as clickable GitHub profile links.

## Requirements

- Python 3.6 or higher.
- A Personal Access Token (PAT) from GitHub for authentication.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/oluizfernando/github-unfollowers.git
   cd github-unfollowers
   ```

2. Install the required libraries:
   ```bash
   pip install requests
   ```

## Usage

1. Run the script:

   ```bash
   python github_unfollowers.py
   ```

2. Enter your GitHub username and Personal Access Token when prompted.

3. The script will output the GitHub profile links of users who don't follow you back.

## Example

```bash
Enter your GitHub username: oluizfernando
Enter your Personal Access Token (PAT): **********
https://github.com/user1
https://github.com/user2
https://github.com/user3
```

## Notes

- Make sure your token has at least the `read:user` scope.
- The script handles pagination automatically to fetch all users, even if you follow many accounts.
- The output provides clickable GitHub profile links. Hold `Ctrl` (or `Cmd` on macOS) and click the link to open it in your browser.

## Limitations

- The GitHub API allows up to 5,000 requests per hour when authenticated with a Personal Access Token (PAT).
- As this is the first version of the program, execution time may increase and take a while depending on the number of users you follow.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
