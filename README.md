# lspack for developers

## How to make a package

### 1. - Make the program in C. In this case, we will make a test package:

- If you have just a single file, call it either `main.c` or `<package-name>.c`.
```c
#include <stdio.h>

int main(void) {
  printf("Hello, world!\n");
  return 0;
}
```

- If you have multiple files, call them as you want and write an `lspack_install_script.sh` like this example:

Example:
```bash
sudo gcc -o /usr/bin/<package-name> file.c otherfile.c otherfile.c
```
*Note: There is no need for error handling in the installation script.*






### 2. - Make a GitHub repository with your package.

- You can now send an [e-mail](mailto:leanderlombardi@gmail.com) to me and if your package is of good quality, I will publish it as an official package.






### 3. - Write a README.md to your package (optional)

It should include the needed commands to install and uninstall your package; such as

```markdown
# package

You can print Hello, world! with my package. Install it:

`lspack install package --author leanderlombardi`

```md

