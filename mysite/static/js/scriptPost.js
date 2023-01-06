console.log("scriptPost");
const postsBox = document.getElementById("posts-box");
const spinnerBoxPost = document.getElementById("spinner-box-posts");
const loadBoxPost = document.getElementById("loading-box-posts");
const loadBtnPost = document.getElementById("load-btn-posts");


fetch("/provide_json_users").then((response) =>
    response.json().then((data) => { 
      users = data.data
      console.log(users)
      console.log("aqui?")

    }))


const ShowMorePosts = () => {
  visiblePost += 3;
  handleGetDataPosts();
};

const ShowLessPosts = () => {
  spinnerBoxPost.classList.remove("not-visible");
  setTimeout(() => {
    spinnerBoxPost.classList.add("not-visible");
    visiblePost = 3;

    postsBox.innerHTML = "";
    loadBoxPost.classList.remove("not-visible");
    handleGetDataPosts();
    document.getElementById("visitorposts").scrollIntoView({behavior: 'smooth'})
  }, 500);


};

let visiblePost = 3;

const handleGetDataPosts = () => {
  fetch(`/provide_json_posts/${visiblePost}`).then((response) =>
    response.json().then((data) => {
      max_size = data.max;
      const posts = data.data;
      spinnerBoxPost.classList.remove("not-visible");
      setTimeout(() => {
        spinnerBoxPost.classList.add("not-visible");
        posts.map((post) => {
          console.log(post.title);
          var selected_date = post.created_at;
          var right_user = post.user_id;
          author = users.filter((x)=>x.id === right_user)[0]


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
          var newDate = new Date(post.created_at);
          var formattedDate =
            newDate.getDay() +
            ", " +
            monthNames[newDate.getMonth()] +
            " " +
            newDate.getFullYear();
          postsBox.innerHTML += `
          
          <hr class="my-4" />
          <div class="post-preview">
          <h4 class="post-title">${post.title}</h2>
          <p style="font-size: large;" class="post-subtitle">${post.content}</p>
          <p class="post-meta">
              Depoimento realizado por ${author.first_name} ${author.last_name}
              em ${formattedDate}
          </p>
          </div>
                
                `;
        });
      }, 500);
      if (max_size) {
        loadBoxPost.classList.add("not-visible");
        console.log("done");

        setTimeout(() => {
          postsBox.innerHTML += `
            <div id="loading-box2-post"><div class="d-flex justify-content-center mb-4"> <a> <button id="load-btn2-post" onclick="ShowLessPosts()" class="btn btn-primary text-uppercase">Mostrar menos</button> </a></div></div>
            `;
        }, 550);

        const loadBtn2Post = document.getElementById("load-btn2-post");
      }
    })
  );
};

handleGetDataPosts();
