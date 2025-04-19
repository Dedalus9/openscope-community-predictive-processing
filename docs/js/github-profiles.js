// GitHub profiles for team members
const GITHUB_PROFILES = {
  // This is a mapping of names to GitHub usernames
  // Add actual usernames as you collect them from team members
  "Jérôme A. Lecoq": "jeromelecoq",
  "André M. Bastos": "andremarcosbastos",
  "Farzaneh Najafi": "fnajafi",
  "Sarah Ruediger": "sruediger",
  // Add more team members and their GitHub usernames here
  // Format: "Full Name": "github-username",
};

// Function to get GitHub username by person's name
function getGitHubUsername(fullName) {
  return GITHUB_PROFILES[fullName] || null;
}

// Export the functions and data for use in other scripts
if (typeof module !== 'undefined') {
  module.exports = {
    GITHUB_PROFILES,
    getGitHubUsername
  };
}

// GitHub Profile Renderer
document.addEventListener('DOMContentLoaded', function() {
    // Find all elements with github-user class
    const githubUsers = document.querySelectorAll('.github-user');
    
    // Process each GitHub user reference
    githubUsers.forEach(function(element) {
        const username = element.textContent.trim().replace('@', '');
        if (!username) return;
        
        // Create profile card container
        const cardContainer = document.createElement('div');
        cardContainer.className = 'github-profile-card';
        
        // Add loading indicator
        cardContainer.innerHTML = `<div class="loading">Loading ${username}'s profile...</div>`;
        
        // Insert card after the element
        element.parentNode.insertBefore(cardContainer, element.nextSibling);
        
        // Fetch GitHub profile data
        fetch(`https://api.github.com/users/${username}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('GitHub profile not found');
                }
                return response.json();
            })
            .then(data => {
                // Create profile card with GitHub data
                cardContainer.innerHTML = `
                    <div class="profile-card">
                        <div class="profile-image">
                            <a href="${data.html_url}" target="_blank">
                                <img src="${data.avatar_url}" alt="${username}'s avatar">
                            </a>
                        </div>
                        <div class="profile-info">
                            <h3><a href="${data.html_url}" target="_blank">${data.name || username}</a></h3>
                            ${data.bio ? `<p class="bio">${data.bio}</p>` : ''}
                            <p class="stats">
                                <span title="Repositories"><i class="fa fa-code-fork"></i> ${data.public_repos}</span>
                                <span title="Followers"><i class="fa fa-users"></i> ${data.followers}</span>
                            </p>
                        </div>
                    </div>
                `;
            })
            .catch(error => {
                cardContainer.innerHTML = `<div class="error">Could not load GitHub profile for ${username}</div>`;
                console.error('Error fetching GitHub profile:', error);
            });
    });
});