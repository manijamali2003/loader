# loader
In the name of God, the Compassionate, the Mericful

Python kernel compiler and Loader (c) 2020 Mani Jamali. Free Software MIT License

# How to compile my Python code to kernel binary?

- Git the loader source code:

```shell script
git clone https://github.com/manijamali2003/loader
cd loader
```

- Create your Python code (kernel.py):

```python
print ("Welcome to my kernel written with Python and Compiled with loader")
print ()
print ("Stop!")
```

- Compile your Python code:

```shell script
python3 pyc.py kernel.py
```

- Run your kernel written with Python:

```shell script
sudo qemu-system-x86_64 -kernel kernel.pyc
```
