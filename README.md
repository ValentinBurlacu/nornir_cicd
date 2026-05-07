# n_nornir_cicd

Simple Nornir and Scrapli lab project for working with Cisco-style device inventories, pushing config, and validating OSPF state.

## What is in this repo

- `02_scrapli.py` sends configuration commands from `configs.txt`
- `03_scrapli.py` renders `templates/ospf.j2` with variables from `group_vars/all.yaml` and pushes the result to devices
- `test_ospf.py` checks OSPF neighbor state and fails if adjacency is not `FULL` or `2WAY`
- `_dev_config.yaml` and `_prod_config.yaml` define separate Nornir inventory entry points
- `_dev_hosts.yaml`, `_prod_hosts.yaml`, `_groups.yaml`, and `_defaults.yaml` provide the inventory data

## Inventory layout

The project is split into two simple environments:

- `dev`: uses `_dev_config.yaml` and `_dev_hosts.yaml`
- `prod`: uses `_prod_config.yaml` and `_prod_hosts.yaml`

Both environments use the same shared group and defaults files.

## Requirements

The dependency list is stored in `req.txt`.

Typical setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r req.txt
```

## Credentials

The scripts expect credentials in environment variables:

```bash
export NORNIR_USERNAME=your_username
export NORNIR_PASSWORD=your_password
```

## Running the scripts

Push commands from `configs.txt`:

```bash
python 02_scrapli.py
```

Render and push the OSPF template using the dev inventory:

```bash
python 03_scrapli.py _dev_config.yaml
```

Validate OSPF neighbors using the prod inventory:

```bash
python test_ospf.py _prod_config.yaml
```

## Notes

- The config files and scripts currently reference absolute paths under `/home/val/cicd`. If you run this repo from another location, update those paths first.
- The active inventory in this repo is centered on Cisco IOS devices grouped under `cisco`.
