console.log("script3");

const projectsBox = document.getElementById("projects-box");
const spinnerBox = document.getElementById("spinner-box");
const loadBox = document.getElementById("loading-box");
const loadBtn = document.getElementById("load-btn");
const mySlug2 = document.getElementById("mySlug2").value;
console.log("funcionou ou n?")
console.log(mySlug2)


const ShowMore = () => {
  visible += 3;
  handleGetData();
};

const ShowLess = () => {
  spinnerBox.classList.remove("not-visible");
  setTimeout(() => {
    console.log("foi agora");
    spinnerBox.classList.add("not-visible");
    visible = 3;

    projectsBox.innerHTML = "";
    loadBox.classList.remove("not-visible");

    handleGetData();
    document
      .getElementById("mainsection")
      .scrollIntoView({ behavior: "smooth" });
  }, 500);
};

let visible = 3;

const handleGetData = () => {
  fetch(`/provide_json/${visible}/${mySlug2}`).then((response) =>
    response.json().then((data) => {
      max_size = data.max;
      const projects = data.data;
      console.log("AQUIIIIII");
      spinnerBox.classList.remove("not-visible");
      setTimeout(() => {
        spinnerBox.classList.add("not-visible");
        projects.map((project) => {
          console.log(project.title);
          var selected_date = project.created_at;

          var monthNames = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ];
          var newDate = new Date(project.created_at);
          var formattedDate =
            newDate.getDate() +
            ", " +
            monthNames[newDate.getMonth()] +
            " " +
            newDate.getFullYear();
          projectsBox.innerHTML += `
          <hr class="my-4" />
            <div class="post-preview">
                <a href="/project/${project.slug}">
                    <h2 class="post-title">${project.title}</h2>
                    <h3 class="post-subtitle">${project.summary}</h3>
                </a>
                <p class="post-meta">
                    Realizaddo por
                    <a href="about.html">Roberto Duarte</a>
                    ${formattedDate}
                </p>
            </div>
                
                `;
        });
      }, 500);
      if (max_size) {
        loadBox.classList.add("not-visible");
        console.log("done");
        console.log("AQUIIIIII");

        setTimeout(() => {
          projectsBox.innerHTML += `
            <div id="loading-box2"><div class="d-flex justify-content-center mb-4"> <a> <button id="load-btn2" onclick="ShowLess()" class="btn btn-primary text-uppercase">Mostrar menos</button> </a></div></div>
            `;
        }, 550);

        const loadBtn2 = document.getElementById("load-btn2");
      }
    })
  );
};

handleGetData();
