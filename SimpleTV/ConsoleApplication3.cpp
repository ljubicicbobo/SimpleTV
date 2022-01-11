// ConsoleApplication3.cpp : Diese Datei enthält die Funktion "main". Hier beginnt und endet die Ausführung des Programms.
//

/*
2. Učitajte niz od 10 cjelobrojinih elemenata. Ispišite aritmetičku sredinu najmanjeg i najvećeg
elementa niza, ali za izračun aritmetičke sredine definirajte funkciju arSredina.

3. U glavnom programu učitaj matricu dimenzije 3 retka i 4 stupca. Korištenjem funkcije sum_mat()
izračunajte sumu svih elemenata matrice.

4. Napišite program koji s tipkovnice učitava riječ (niz od max. 50 velikih slova abecede) te ispisuje
koliko riječ ima samoglasnika. Definirajte funkciju brojiSamoglasnike() za brojanje samoglasnika u
riječi.

5. Definirajte 3 funkcije:
Prva neka izračunava aritmetičku sredinu dva cijela broja.
Druga funkcija neka izdvaja najveći element niza.
Treća funkcija neka izdvaja najmanji element niza.
Zatim, u glavnom dijelu programa učitajte niz od 10 cjelobrojnih elemenata, te ispišite aritmetičku
sredinu najmanjeg i najvećeg elementa niza, izračunavanjem vrijednosti pomoću prethodno
definiranih funkcija.

6. Neka korisnik unese 10 cjelobrojnih elemenata niza. U funkciji izračunajte koliko je elemenata veće
od aritmetičke sredine niza. Rezultat ispišite u glavnom dijelu programa.


*/
#include <iostream>

int arSredina(float a, float b) {
    float arSred;
    arSred = a + b / 2;
    printf("Aritmeticka sredina je %f\n", arSred);
    return arSred;
}

int najmanji(int niz[], int vel) {
    int i;
    int nmj = niz[0];
    for (int i = 0; i <= vel; i++) {
        if (niz[i] < nmj)
            nmj = niz[i];
    }

    printf("Najmanji je %d\n", nmj);
    return nmj;
}

int najveci(int niz[], int vel) {
    int i;
    int nmj = niz[0];
    for (int i = 0; i <= vel; i++) {
        if (niz[i] > nmj)
            nmj = niz[i];
    }

    printf("Najveci je %d\n", nmj);
    return nmj;
}

int sumMatrice(int matrica[3][4]) {
    int i, j, suma;
    suma = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++)
            suma += matrica[i][j];
    }
    printf("Suma je %d\n", suma);
    
    return suma;
}

int arSredinaSve(int niz[]) {
    int i;
    int arSred;
    int s = 0;
    for (i = 0; i < 9; i++) {
            s += niz[i];
    }
    
    int n = 0;
    arSred = s / 10;
    for (i = 0; i < 9; i++) {
        if (niz[i] > arSred)
            ++n;
    }

    return n;
}
// a, e, i, o, u
char brojanjeSamoglasnika(char rijec[]) {
    int i;
    int br = 0;
    for (i = 0; i <= sizeof(&rijec); i++) {
        if (rijec[i] == 'a' || rijec[i] == 'e' || rijec[i] == 'i' || rijec[i] == 'o' || rijec[i] == 'u')
            br++;
    }
    return br;
}

int main()
{
    // 2
    int ml, vl;
    int niz[10] = { 1,2,3,4,5,6,7,8,9 };
    ml = najmanji(niz, 9);
    vl = najveci(niz, 9);
    arSredina(ml, vl);

    // 3
    int mat[3][4] = { {1, 2, 3, 4}, {4, 5, 6, 7}, {2, 4, 9, 0}};
    sumMatrice(mat);

    // 4
    char rijeci[50];
    printf("Unesite rijec od max 50 char: \n");
    //scanf_s(" %c", &rijeci, 50);
    fgets(rijeci, sizeof(rijeci), stdin);

    printf("%d\n ", brojanjeSamoglasnika(rijeci));

    // 5
    int niz2[10] = { 1,2,3,4,5,6,7,8,9 };
    ml = najmanji(niz, 9);
    vl = najveci(niz, 9);
    arSredina(ml, vl);

    // 6
    printf("Unesite 10 cijelih brojeva niza: \n");
    int niz3[10];
    for (int i = 0; i < 10; i++) {
        scanf_s("%d", &niz3[i]);
    }
    int n = arSredinaSve(niz3);
    printf("Vecih je %d\n", n);

    return 0;
}

/*

4. Napišite program koji s tipkovnice učitava riječ (niz od max. 50 velikih slova abecede) te ispisuje
koliko riječ ima samoglasnika. Definirajte funkciju brojiSamoglasnike() za brojanje samoglasnika u
riječi.

*/


// Programm ausführen: STRG+F5 oder Menüeintrag "Debuggen" > "Starten ohne Debuggen starten"
// Programm debuggen: F5 oder "Debuggen" > Menü "Debuggen starten"


// Tipps für den Einstieg: 
//   1. Verwenden Sie das Projektmappen-Explorer-Fenster zum Hinzufügen/Verwalten von Dateien.
//   2. Verwenden Sie das Team Explorer-Fenster zum Herstellen einer Verbindung mit der Quellcodeverwaltung.
//   3. Verwenden Sie das Ausgabefenster, um die Buildausgabe und andere Nachrichten anzuzeigen.
//   4. Verwenden Sie das Fenster "Fehlerliste", um Fehler anzuzeigen.
//   5. Wechseln Sie zu "Projekt" > "Neues Element hinzufügen", um neue Codedateien zu erstellen, bzw. zu "Projekt" > "Vorhandenes Element hinzufügen", um dem Projekt vorhandene Codedateien hinzuzufügen.
//   6. Um dieses Projekt später erneut zu öffnen, wechseln Sie zu "Datei" > "Öffnen" > "Projekt", und wählen Sie die SLN-Datei aus.
