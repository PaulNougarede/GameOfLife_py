#include "header.h"

//0 = morte / 1 = vivante / 2 = va mourrir / 3 = va vivre

t_cell** init()
{
    int i,j;
    t_cell** tab = (t_cell**)malloc(X * sizeof(t_cell*));
    for(i = 0; i<X; i++)
    {
        tab[i] = (t_cell*)malloc(X * sizeof(t_cell));
    }
    for(i = 0; i<X; i++)
    {
        for(j = 0; j<X; j++)
        {
            tab[i][j].etat = 0;
            tab[i][j].next = 0;
        }
    }
    for(i = 90 ; i< 110 ; i++)
    {
        for(j = 90 ; j< 110 ; j++)
        {
            tab[i][j].etat = rand()%2;
        }
    }
    return tab;

}

void jeu()
{
    initialisationAllegro();
    int compteur = 0,tour = 10000, count = 0, stop = 0;
    srand(time(NULL));
    t_cell** tab = init();
    aff_alleg(tab, compteur);
    while(compteur != tour && stop != 1)
    {
        if(key[KEY_ESC])
            stop = 1;
        else
        {
            for(int i = 1; i<X-1; i++)
            {
                for(int j = 1; j<X-1; j++)
                {
                    count = 0;
                    if(tab[i-1][j-1].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i-1][j].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i-1][j+1].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i][j-1].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i][j+1].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i+1][j-1].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i+1][j].etat == 1)
                    {
                        count+=1;
                    }
                    if(tab[i+1][j+1].etat == 1)
                    {
                        count+=1;
                    }
///regles------------------------------------------------------------------------------
                    if(tab[i][j].etat == 0 && count == 3)
                    {
                        tab[i][j].next = 1;
                    }
                    if(tab[i][j].etat == 1 && (count != 2 && count != 3))
                    {
                        tab[i][j].next = 0;
                    }
                    if(tab[i][j].etat == 0 && count == 0 && compteur < 100)
                    {
                        if(rand()%500 == 1)
                            tab[i][j].next = rand()%2;
                    }
                }
            }
            for(int i = 1; i<X-1; i++)
            {
                for(int j = 1; j<X-1; j++)
                {
                    if(tab[i][j].next == 0)
                        tab[i][j].etat = 0;
                    else if(tab[i][j].next == 1)
                        tab[i][j].etat = 1;
                }
            }
        }
        compteur += 1;
        aff_alleg(tab,compteur);
        Sleep(500);
    }
    while(!key[KEY_ESC])
    {
        aff_alleg(tab, compteur);
    }
}



