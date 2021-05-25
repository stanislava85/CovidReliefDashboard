import streamlit as st
import streamlit.components.v1 as components


def app():
    st.title('Meet the team')
    # bootstrap 4 collapse example
    components.html(
        """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"
    integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js"
    integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT"
    crossorigin="anonymous"></script>
    <div class="container" style="margin-top: 100px;">
      <div class="row">
        <div class="col">
          <div class="card" style="width: 18rem">
            <img width="400px" height="250px"
              src="https://avatars2.githubusercontent.com/u/65839965?height=180&v=4&width=180" class="card-img-top"
              alt="..." />
            <div class="card-body">
              <h5 class="card-title">Clariza Mayo</h5>
              <p class="card-text">
                Clariza is an Ambitious data science fellow with diverse skill sets, technical proficiencies and new perspectives to leadership personnel. Adaptable
                and driven with strong work ethic and ability to thrive in team-based or individually motivated
                settings.
              </p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card" style="width: 18rem">
            <img width="400px" height="250px"
              src="https://stanislava85.github.io/Website/img/MotherCoders-Stanislava.JPG" class="card-img-top"
              alt="..." />
            <div class="card-body">
              <h5 class="card-title">Stanislava Hristova</h5>
              <p class="card-text">
             Stanislava is a life-long learner with a background in Marketing and a passion for Data Science & Cybersecurity Awareness. Capable of effectively bridging the gap between Business and Engineering teams by rendering excellent technical and communication skills.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <div class="card" style="width: 18rem">
            <img width="400px" height="250px" src="https://avatars.githubusercontent.com/u/23387540?v=4"
              class="card-img-top" alt="..." />
            <div class="card-body">
              <h5 class="card-title">Juan Peralta</h5>
              <p class="card-text">
                Juan is a business Intelligence Analyst, Experienced on T-SQL Data Engineering, Analytics & Programming. Juan is very familiarized with Systems SLDC analysis, design, development, implementation and
                support. Finally, Juan proficient in Microsoft BI Data tools.
              </p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card" style="width: 18rem">
            <img width="400px" height="250px" src="https://avatars.githubusercontent.com/u/36942613?s=400&v=4"
              class="card-img-top" alt="..." />
            <div class="card-body">
              <h5 class="card-title">Kari Sakib</h5>
              <p class="card-text">
                Kari is a Data Analyst and a multi-disciplinary tech enthusiast aspiring to be a Machine Learning
                Engineer. His flexibility with modern day technologies allows him to build fine projects with great
                detail. He spends his time pursuing opprtunities of great advancements and projects to develop and
                sharpen his skillset.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

        """,
        height=1500,
    )
