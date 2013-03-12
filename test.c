#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <termios.h>

#define QUIT_CHAR 0x04 /* CTRL-D を押すと終了する．*/
#define MAIN

int getch();
void exitfunc(void);

// 端末設定保存用大域変数
static struct termios CookedTermIos; // cooked モード用
static struct termios RawTermIos; // raw モード用

int getch()
{
	static int is_stating = 0;
	if (is_stating == 0){
		tcgetatr(STDIN_FILENO, &CookedTermIos);

		RawTermIos = CookedTermIos;
		cfmakeraw(&RawTermIos);

		tcsetattr(STDIN_FILENO, 0, &RawTermIos);
		atexit(exitfunc);
	}

	return (0);
}

void exitfunc(void)
{
	tcsetattr(STDIN_FILENO, 0, &CookedTermIos);
}

#ifdef MAIN
int main(int argc, char const* argv[])
{
	char c;
	while ((c = getch()) != QUIT_CHAR){
		printf("%c\n", c);
	}

	return 0;
}

#endif
