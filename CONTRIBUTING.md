# Contributing to LAPGCCraft

You can suggest changes to the pack. Jeremy reviews every change before it goes live. Nothing reaches the server or your friends' game until it's approved.

There are two ways to contribute. Pick whichever is easier for you.

## Option A: Edit on GitHub (no extra software)

Good for small changes, such as editing a config value or a KubeJS script.

1. Sign in to GitHub and open the file you want to change in the repo, under `overrides/`.
2. Click the pencil icon (**Edit this file**). GitHub will make a copy of the repo under your account, called a **fork**.
3. Make your change and write a short message describing it.
4. Click **Propose changes**, then **Create pull request**.
5. Fill in the template and submit.

## Option B: Use Packweave (for mod additions and bigger changes)

Packweave is the tool used to build the pack. Use it for adding or removing mods, or for larger changes.

1. Install Packweave from packweave.com.
2. On GitHub, click **Fork** at the top of the repo page. This creates your own copy.
3. In Packweave, clone **your fork** (not the main repo) and make a new branch for your change.
4. Make your change. Test it in singleplayer if you can.
5. Commit the change and push the branch to your fork.
6. On GitHub, open your fork and click **Compare & pull request**. Fill in the template and submit.

## What happens next

- An automatic check runs on your pull request. If it finds a problem, it tells you what to fix. Push a new commit to the same branch to update the pull request.
- Jeremy reviews the change and either approves it or asks for changes.
- Once approved, the server updates on its own within about 5 minutes. Restart-level changes wait until the server is empty, and players get a warning first.
- Players receive client-side changes the next time they start the game, once Jeremy publishes a new pack version.

## Rules

- **Don't add mod jar files by hand.** Add mods through Packweave so they're recorded properly.
- **Don't include personal files.** That means map data, saves, options, and server settings.
- **Keep changes small and focused.** One change per pull request makes review easier.
- **Test before you submit** if you can.

## Stuck?

Ask in Discord. Nobody will judge you for asking.
