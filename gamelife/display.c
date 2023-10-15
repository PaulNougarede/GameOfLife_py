#include "header.h"

void initialisationAllegro()
{
    allegro_init();
    set_color_depth(desktop_color_depth());
    if((set_gfx_mode(GFX_AUTODETECT_WINDOWED,700,700,0,0))!=0)
    {
        allegro_message("Pb de mode graphique") ;
        allegro_exit();
        exit(EXIT_FAILURE);
    }
    install_keyboard();
    install_mouse();
    show_mouse(screen);
}

void affichetab(t_cell** tab, int compteur)
{
    system("cls");
    for(int i = 0; i<X; i++)
    {
        for(int j = 0; j<X; j++)
        {
            if(tab[i][j].etat == 0)
                printf(" ");
            if(tab[i][j].etat == 1)
                printf("%c", 254);
        }
        printf("\n");
    }
    printf("%d ", compteur);
    system("PAUSE");
}

void aff_alleg(t_cell** tab, int compteur)
{
    BITMAP* fond = create_bitmap(SCREEN_W-100, SCREEN_H-100);
    for(int i = 0; i<X; i++)
    {
        for(int j = 0; j<X; j++)
        {
            if(tab[i][j].etat == 0)
                rectfill(fond,3*i,3*j,(3*i)+3,(3*j)+3,makecol(255,255,255));
            else if(tab[i][j].etat == 1)
                rectfill(fond,3*i,3*j,(3*i)+3,(3*j)+3,makecol(0,0,0));
        }
    }
    textprintf_ex(fond, font, 0,1,makecol(0,0,0), makecol(255,255,255),"TOUR : %d",compteur);
    blit(fond, screen, 0,0,50,50,SCREEN_W, SCREEN_H);
    destroy_bitmap(fond);
}




