
name = "avalon_sftpc"

description = "Avalon SFTP Client, for uploading Avalon workfile or " \
              "representation to remote site via SFTP"

version = "0.3.0"

authors = [
    "davidlatwe",
]


tools = [
    "python -m avalon_sftpc --demo",
]

requires = [
    # Dependencies
    "avalon",
    "pysftp",
]


private_build_requires = ["rezutil-1"]
build_command = "python {root}/rezbuild.py {install}"


# Set up environment
def commands():
    env = globals()["env"]
    env.PYTHONPATH.prepend("{root}/payload")

    # This is required.
    # env.AVALON_SFTPC_SITES = ""
