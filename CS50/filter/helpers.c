#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int h = 0; h < width; h++)
        {
            double average = (image[i][h].rgbtRed + image[i][h].rgbtBlue + image[i][h].rgbtGreen) / 3.0;
            //a stands for the rounded average
            int a = round(average);

            //all need to be equal for gray
            image[i][h].rgbtRed = a;
            image[i][h].rgbtBlue = a;
            image[i][h].rgbtGreen = a;

        }
    }

    return;

}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int h = 0; h < width; h++)
        {

            float sepiaRed, sepiaGreen, sepiaBlue;
            sepiaRed = round((image[i][h].rgbtRed * .393) + (image[i][h].rgbtGreen * .769) + (image[i][h].rgbtBlue * .189));
            sepiaGreen = round((image[i][h].rgbtRed * .349) + (image[i][h].rgbtGreen * .686) + (image[i][h].rgbtBlue * .168));
            sepiaBlue = round((image[i][h].rgbtRed * .272) + (image[i][h].rgbtGreen * .534) + (image[i][h].rgbtBlue * .131));


            image[i][h].rgbtRed = sepiaRed;
            image[i][h].rgbtGreen = sepiaGreen;
            image[i][h].rgbtBlue = sepiaBlue;

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
                image[i][h].rgbtRed = sepiaRed;
            }
            return;

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
                image[i][h].rgbtGreen = sepiaGreen;
            }
            return;

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
                image[i][h].rgbtBlue = sepiaBlue;
            }
            return;


        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int h = 0; h < (width / 2); h++)
        {
            int R = image[i][h].rgbtRed;
            int G = image[i][h].rgbtGreen;
            int B = image[i][h].rgbtBlue;

            image[i][h].rgbtRed = image[i][width - h - 1].rgbtRed;
            image[i][h].rgbtGreen = image[i][width - h - 1].rgbtGreen;
            image[i][h].rgbtBlue = image[i][width - h - 1].rgbtBlue;

            image[i][width - h - 1].rgbtRed = R;
            image[i][width - h - 1].rgbtGreen = G;
            image[i][width - h - 1].rgbtBlue = B;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE make[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int h = 0; h < width; h++)
        {
            int avgRed = 0;
            int avgGreen= 0;
            int avgBlue = 0;
            float blocks = 0;

            for (int x = -1; x < 2; x++)
            {
                for (int z = -1; z < 2; z++)
                {
                    if(i + x < 0 || i + x > height - 1 || h + z < 0 || h + z > width - 1)
                    {
                        continue;
                    }

                    avgRed = avgRed + image[i + x][h + z].rgbtRed;
                    avgGreen = avgGreen + image[i + x][h + z].rgbtGreen;
                    avgBlue = avgBlue + image[i + x][h + z].rgbtBlue;

                    blocks++;
                }

            }

            make[i][h].rgbtRed = round(avgRed / blocks);
            make[i][h].rgbtGreen = round(avgGreen / blocks);
            make[i][h].rgbtBlue = round(avgBlue / blocks);

        }
    }
     for (int i = 0; i < height; i++)
    {
        for (int h = 0; h < width; h++)
        {
            image[i][h].rgbtRed = make[i][h].rgbtRed;
            image[i][h].rgbtGreen = make[i][h].rgbtGreen;
            image[i][h].rgbtBlue = make[i][h].rgbtBlue;
        }
    }
    return;
}
