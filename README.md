# Live-Football
A tool to fetch the live scores from the football matches around the world


<h1>Usage</h1>

<p> This program makes use of <a href="https://allsportsapi.com/">All Sports API</a>. 
<p> The standard API key for LIVE results is of the form : 
  
  ```
  https://allsportsapi.com/api/football/?met=Livescore&APIkey=<insert your API key here>
  ```
<p> That said, the URL can be tweaked to get other statistics as well. If you want results from specific leagues, then append <i>&leagueId=</i> after <i>?met=Livescore</i> followed by the actual id. For example, if you want to get scores from the English Premier League only, then your API call would look something like this :</p>

  ```
  https://allsportsapi.com/api/football/?met=Livescore&leagueId=148&APIkey=<insert your API key here>
  ```
<p> Similarly, the results can be refined according to the user's needs. To know more details about how to get specific results, check this <a href="https://allsportsapi.com/soccer-football-api-documentation">documentation</a>.</p>

<p> For reference, I am adding the leagueId for the top 5 leagues:</p><br>
  
  ``` 
  English Premier League - #148 
  Spanish LaLiga         - #468
  Serie A                - #262
  Bundesliga             - #195
  Ligue 1                - #176
  ```

<p> To check the league codes for specific leagues, check this <a href="https://allsportsapi.com/soccer-football-api-coverage">link</a>.</p>

<br><p> Once, you get your API, you can proceed to the following</p>
<ol type="I">
  <li> Clone or download the repository in your preferred directory</li><br>

  ```
  git clone https://github.com/InvincibleJuggernaut/Live-Football.git
  ```
  <br>
  <li> Open the repository folder and open the file <i>core_code.py</i> and insert your API key in the code where its needed.</li>
  <br>
  <li> Save the code and go back to the repository</li>
  <br>
  <li> Now, open the terminal inside the repository folder</li>
  <br>
  <li> Run the program using</li><br>  

```
python core_code.py
```
</ol>
