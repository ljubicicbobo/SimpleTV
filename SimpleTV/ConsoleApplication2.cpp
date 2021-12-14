// ConsoleApplication2.cpp : Diese Datei enthält die Funktion "main". Hier beginnt und endet die Ausführung des Programms.
//

#include <iostream>
#include <stdio.h>
#define MESG "COMPUTER BYTES DOG"
#define TEN 10

int main()
{
    /*
    int i, a[10] = { 2,4,6,8,10,1,3,5,7,9 };
    int min = a[0], max = a[0];
    float arSred;
    for (i = 0; i < 10; i++) {
        if (a[i] < min)
            min = a[i];
        if (a[i] > max)
            max = a[i];
    }
    arSred = (min + max) / 2.0;
    printf("Namanji element niza je %d\n", min);
    printf("Aritmeticka sredina najmanjeg i najveceg elementa je %f\n", arSred);

    // 2
    int j, b[10] = { 0,1,2,3,4,5,6,7,8,9 };
    j = 0;
    for (i = 1; i < 9; ++i) {
        j += b[i];
    }
    printf("%d\n", j);

    // 3
    int c[4] = {0};
    int cc = 0;
    int d[6] = {0};
    int dd = 0;
    for (i = 0; i < 10; i++) {
        if (b[i] % 3 == 0) {
            c[cc] = b[i];
            ++cc;
        }
        else {
            d[dd] = b[i];
            ++dd;
        }
    }
    for (i = 0; i < 4; i++) {
        printf("%d  ", c[i]);
    }
    printf("\n\n");
    for (i = 0; i < 6; i++) {
        printf("%d  ", d[i]);
    }
    printf("\n\n");

    // 4 
    int noviNiz[4] = { 0 };
    printf("Unesite niz od 4 broja: ");
    j = 0;
    for (i = 0; i < 4; i++) {
        scanf_s("%d", &noviNiz[i]);
        j += noviNiz[i];
    }
    arSred = j / 3;

    for (i = 0; i < 4; i++) {
        if (noviNiz[i] < arSred) {
            printf("%d  ", noviNiz[i]);
        }
    }
    printf("\n\n");
    printf("Veci su: ");
    for (i = 0; i < 4; i++) {
        if (noviNiz[i] > arSred) {
            printf("%d  ", noviNiz[i]);
        }
    }
    printf("\n\n");
    printf("Jednaki: ");
    for (i = 0; i < 4; i++) {
        if (noviNiz[i] == arSred) {
            printf("%d  ", noviNiz[i]);
        }
    }
    */
    // 5
    int i, j;
    int matrica[2][2] = { {0}, {0} };
    printf("Unesite elemente matrice 5x5\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            scanf_s("%d", &matrica[i][j]);
        }
    }

    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", matrica[i][j]);
        }
        printf("\n");
    }

    int najmanji = matrica[1][1];
    printf("\n\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            if (matrica[i][j] < najmanji)
                najmanji = matrica[i][j];
        }
    }
    printf("Najmanji broj je: %d\n", najmanji);
    int najmanjiGlavna = matrica[1][1];
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            if (matrica[i][j] < najmanjiGlavna && i == j)
                najmanjiGlavna = matrica[i][j];
        }
    }
    printf("Najmanji element na glavnoj djagonali je: %d\n", najmanjiGlavna);
    int najmanjiSporedna = matrica[0][1];
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            if (matrica[i][j] < najmanji && i != j)
                najmanjiSporedna = matrica[i][j];
        }
    }
    printf("Najmanji element na sporednim dijagonalama je: %d\n", najmanjiSporedna);

    return 0;
}

// Programm ausführen: STRG+F5 oder Menüeintrag "Debuggen" > "Starten ohne Debuggen starten"
// Programm debuggen: F5 oder "Debuggen" > Menü "Debuggen starten"

// Tipps für den Einstieg: 
//   1. Verwenden Sie das Projektmappen-Explorer-Fenster zum Hinzufügen/Verwalten von Dateien.
//   2. Verwenden Sie das Team Explorer-Fenster zum Herstellen einer Verbindung mit der Quellcodeverwaltung.
//   3. Verwenden Sie das Ausgabefenster, um die Buildausgabe und andere Nachrichten anzuzeigen.
//   4. Verwenden Sie das Fenster "Fehlerliste", um Fehler anzuzeigen.
//   5. Wechseln Sie zu "Projekt" > "Neues Element hinzufügen", um neue Codedateien zu erstellen, bzw. zu "Projekt" > "Vorhandenes Element hinzufügen", um dem Projekt vorhandene Codedateien hinzuzufügen.
//   6. Um dieses Projekt später erneut zu öffnen, wechseln Sie zu "Datei" > "Öffnen" > "Projekt", und wählen Sie die SLN-Datei aus.
