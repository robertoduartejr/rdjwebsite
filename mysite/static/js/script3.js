console.log("script3")
const projectsBox = document.getElementById('projects-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBox = document.getElementById('loading-box')
const loadBtn = document.getElementById('load-btn')


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
                var selected_date = project.created_at.oLocaleDateString("en-US")
                projectsBox.innerHTML +=`
            <div class="post-preview">
                <a href="/project/${project.slug}">
                    <h2 class="post-title">${project.title}</h2>
                    <h3 class="post-subtitle">${project.summary}</h3>
                </a>
                <p class="post-meta">
                    Realizaddo por
                    <a href="about.html">Roberto DuarteTESTE</a>
                    ${selected_date}
                </p>
            </div>
                
                `
            })
        }, 500);
        if(max_size){
            console.log("done")
        }

        }))
}
    

handleGetData()
loadBtn.addEventListener('click', () => {
    visible +=3
    handleGetData()
})

function join(t, a, s) {
    function format(m) {
       let f = new Intl.DateTimeFormat('en', m);
       return f.format(t);
    }
    return a.map(format).join(s);
 }
 
 let a = [{day: 'numeric'}, {month: 'short'}, {year: 'numeric'}];
 let s = join(new Date, a, '-');
 console.log(s);