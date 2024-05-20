<script>

  
  
</script>


<nav class="headlogo">
  <div class="logo">
    <a href="/">TRAIN Booking</a>
    
  </div>
  <div class="headlogo">
    <div class="logo">
    <a href="/history">TRAIN History</a>
    
    
  </div>
</nav>



<slot></slot>

<footer>
<footer class="footer">
    <div class="content">
      <p>About us</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore maiores asperiores alias quod expedita illum assumenda? Dolores esse excepturi, atque beatae incidunt accusantium nemo libero vitae consectetur exercitationem maiores voluptates!</p>
    </div>
     <div class="contact">
      <p>Contact us</p>
      <a href="/"><i class="fa-brands fa-facebook"></i>Website</a>
      <a href="/"><i class="fa-brands fa-facebook"></i>Tel. 0123456789</a>
    </div>
  </footer>
</footer>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}


nav.headlogo {
  background-color: #2c3e50;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}


nav.headlogo .logo {
  display: flex;
  align-items: center;
}

nav.headlogo .logo a {
  color: #ecf0f1;
  text-decoration: none;
  font-size: 24px;
  font-weight: bold;
  margin-right: 20px;
  transition: color 0.3s ease;
}

nav.headlogo .logo a:hover {
  color: #3498db;
}


nav.headlogo .buttons a {
  background-color: #3498db;
  color: white;
  padding: 10px 15px;
  text-decoration: none;
  border-radius: 4px;
  margin-left: 10px;
  transition: background-color 0.3s ease;
}

nav.headlogo .logo a {
  border: 2px solid ; 
  padding: 5px;
  border-radius: 5px; 
}

nav.headlogo .buttons a:hover {
  background-color: #2980b9;
}


@media (max-width: 768px) {
  nav.headlogo {
    flex-direction: column;
    align-items: flex-start;
  }

  nav.headlogo .logo a {
    margin-bottom: 10px;
  }



  nav.headlogo .buttons a {
    margin: 5px 0;
    width: 100%;
    text-align: center;
  }
}



.footer {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  background-color: #f0f0f0;
}

.footer .content,
.footer .contact {
  width: 45%;
}
.footer a {
  display: block;
  margin-bottom: 5px;
  text-decoration: none;
  color: #333;
}

.footer p {
  margin-bottom: 20px;
}


nav {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background-color: hsl(29, 81%, 51%);
}

.logo a {
  text-decoration: none;
  color: aliceblue;
  font-weight: bold;
  
}




</style>