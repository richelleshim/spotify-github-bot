# spotify-github-bot

# Spotify GitHub Bot

LMAO IM SO DUMB... my `.git` folder isn't in this repo, so that sucks... will fix this with proper directions but it works for me right now !!

## Description
**Spotify GitHub Bot**: whenever you commit, it shows you what you were listening to at the time of the commit !! which is actually so cutesie and so slay ?! hello ?!

### Current Status
- Code is in my `.git` folder.
- uh: code is in my .git folder and i'm kind of procrastinating with putting code because one time i screwed up and pushed a file and revealed my api key which was the dumbest mistake and i'm never doing that again i swear i learned my lesson...


---

## To-Do [Needs Fixing]
- Properly move the code from `.git` to this repository.
- Improve this README with a better explanation.
- Fix the directions to ensure easier setup for others.

---

## Directions

1. **Set up Environment Variables**:
   - Rename the `.env-copy` file to `.env`.
   - Fill in the required values for your specific configuration.

2. **Update Hook Path**:
   - Update the path in `prepare-commit-msg` located in `.git/hooks/prepare-commit-msg` to match your setup.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Git Hook**:
   ```bash
   python3 scripts/setup_git_hook.py
   ```

5. **Debug Issues**:
   - Run the bot and ensure it works as expected.
   - Fix any errors that arise during the setup process (I probably forgot something, sorry!).

rev3


/Users/richelleshim/spotify-git-bot/.git/hooks/setup_git_repo.sh

mv /Users/richelleshim/spotify-git-bot/.git/hooks/setup_git_repo.sh ~/.local/bin/
