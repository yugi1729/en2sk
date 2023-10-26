# en2sk
a simple python cli script to get equivalent sanskrit words for english words.

## Sample Output :
|      Dev.      | grammar |      IAST       | En. Word | En. Add |
|:--------------:|:-------:|:---------------:|:--------:|:-------:|
| सङ्गणकयन्त्र |    n.   | saṅgaṇakayantra | computer |         |
|   सङ्गणक      |    n.   |    saṅgaṇaka    | computer |         |
|  गणकयन्त्र   |    n.   |   gaṇakayantra  | computer |         |
|  सङ्गणित्र   |    n.   |    saṅgaṇitra   | computer |         |

## Install on Unix-like Systems
- Clone the repo `git clone https://github.com/yugi1729/en2sk.git`
- Change directory to en2sk `cd en2sk`
- make scripts executable `chmod +x en2sk.py; chmod +x run_en2sk`
- Optional step : copy program to /usr/bin `sudo cp run_en2sk /usr/bin/`
- Run `run_en2sk`
