#ifndef HEADER_H_INCLUDED
#define HEADER_H_INCLUDED

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <allegro.h>
#define X 201

typedef struct cellule
{
    int etat;
    int next;
}t_cell;



//allegro
void initialisationAllegro();
void aff_alleg(t_cell** tab, int compteur);
void config_deb();

//display
void affichetab(t_cell** tab, int compteur);

//ssprg
t_cell** init();
void en_vie(t_cell** tab, int l, int c);
void jeu();

#endif // HEADER_H_INCLUDED
