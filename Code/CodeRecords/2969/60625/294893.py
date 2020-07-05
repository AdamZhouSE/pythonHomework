char s[1 << 21];
int x, y, z;
main() {
    int check=0;
    scanf("%s", s);
    while (s[x]) {
        y = z = x;
        while (s[++y] && s[y] >= s[z]) s[y] > s[z++] && (z = x);
        while (x <= z)
        { 
            if (check==0){
                printf("%d", x += y - z);
                check++;
            }
            else printf(" %d", x += y - z);
        }
    }
    printf("\n");
}