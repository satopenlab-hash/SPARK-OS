# Start Here — Upload OpenLab OS to GitHub

This is the simplest path.

## 1. Create a repository

On GitHub:

1. Click **New repository**.
2. Name it `openlab-os`.
3. Choose **Private** for now.
4. Leave the README option unchecked, because this package already has one.
5. Click **Create repository**.

## 2. Upload this package

After you download and unzip `openlab-os-v0.1.0.zip`:

1. Open the new GitHub repository.
2. Click **Add file** → **Upload files**.
3. Drag the **contents inside** the `openlab-os` folder into GitHub.
   - Do not upload the outer ZIP file unless GitHub explicitly accepts it as an import.
4. Scroll down.
5. Commit message:

```text
Initialize OpenLab OS v0.1.0
```

6. Click **Commit changes**.

## 3. Verify the first screen

At the top level, GitHub should show:

```text
CLAUDE.md
README.md
START_HERE.md
skills/
templates/
examples/
sources/
brain/
learning/
recognition/
```

If you see a second nested folder such as `openlab-os/openlab-os/`, go back and upload the files **inside** the folder instead.

## 4. First AI instruction

When using Claude, ChatGPT, Copilot, or another AI with access to this repository, begin with:

```text
Read CLAUDE.md before taking any action.
Then identify the OpenLab layer for this task.
Use the relevant file in skills/.
Do not create files until you can explain where they belong.
```

## 5. First human task

Do one small artifact only:

```text
Create a synthetic classroom mission using templates/mission-template.md.
```

Then run the workflow:

```text
Plan → Build → Check → Human Review → Improve → Document
```

## Do not do these yet

- Do not upload real student work.
- Do not create a public credential system.
- Do not build a multi-agent fleet.
- Do not ask an AI to grade students automatically.

The first goal is a clean, trustworthy foundation.
