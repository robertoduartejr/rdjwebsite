console.log("script3")
const projectsBox = document.getElementById('projects-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBox = document.getElementById('loading-box')
const loadBtn = document.getElementById('load-btn')

const ShowMore = () => {
    visible +=3
    handleGetData()
}

const ShowLess = () => {

    spinnerBox.classList.remove('not-visible')
    setTimeout(() => {
            console.log("foi agora")
            spinnerBox.classList.add('not-visible')
            visible = 3

    projectsBox.innerHTML = ""
    loadBox.classList.remove('not-visible')
    handleGetData()
        
        },500)

}


let visible = 3

const handleGetData = () => {
    fetch(`/provide_json/${visible}`).then(response => response.json().then(data => {
        max_size = data.max
        const projects = data.data
        spinnerBox.classList.remove('not-visible')
        setTimeout(() => {
            spinnerBox.classList.add('not-visible')
            projects.map(project=>{
                console.log(project.title)
                var selected_date = project.created_at

                var monthNames = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ];
                var newDate = new Date(project.created_at);
                var formattedDate = newDate.getDay() + ', ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear();
                projectsBox.innerHTML +=`
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
                
                `
            })
        }, 500);
        if(max_size){
            loadBox.classList.add('not-visible')
            console.log("done")

            setTimeout(() => {
            projectsBox.innerHTML +=`
            <div id="loading-box2"><div class="d-flex justify-content-center mb-4"> <a> <button id="load-btn2" onclick="ShowLess()" class="btn btn-primary text-uppercase">Mostrar menos</button> </a></div></div>
            `},550)
            
            const loadBtn2 = document.getElementById('load-btn2')

        }

        }))
}
    

handleGetData()







